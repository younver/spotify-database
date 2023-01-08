import csv
import argparse
from dataset import *
from converter import *
from database import Database
import mysql.connector

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--port", default="3306")
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="admin")
parser.add_argument("--password", default="")
parser.add_argument("--path", default="../datasets/spotify_dataset_100.csv")
args = parser.parse_args()

# Initialize the database
db = Database(args)

#---------------------------------------------

# Read csv file excluding column names
rows = None
with open(args.path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    rows = [row for row in csv_reader][1:]

#---------------------------------------------

# Clear and insert genre metrics
db.clear_genre_metrics()
genres = []
genre_id = 0
for row in rows:

    print("checking genre metrics", row[COL_ARTIST_NAME])

    # Extract artist genres
    artist_genres = str_to_list(row[COL_ARTIST_GENRES])

    # Insert new genres to genre metrics
    for artist_genre in artist_genres:
        if artist_genre not in genres:
            genres.append(artist_genre)
            db.insert_artist_genre_metric(genre_id, artist_genre)
            genre_id += 1

#---------------------------------------------

# Clear and insert feature metrics
db.clear_feature_metrics()
feature_id = 0
for feature in features:
    db.insert_track_feature_metric(feature_id, feature)
    feature_id += 1

#---------------------------------------------

# Load already existing ids
track_ids = db.get_track_ids()
album_ids = db.get_album_ids()
artist_ids = db.get_artist_ids()

# Insert track - album - artist
for row in rows:

    print("inserting", row[COL_TRACK_INDEX])

    #---------------------------------------------

    week = date_to_str(row[COL_WEEK])

    # Insert weekly track - album - artist
    try:
        db.insert_track_weekly(week=week, rank=row[COL_RANK], streams=row[COL_STREAMS], track_id=row[COL_TRACK_ID], track_popularity=row[COL_TRACK_POP])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)
    try:
        db.insert_album_weekly(week=week, album_popularity=row[COL_ALBUM_POP], album_id=row[COL_ALBUM_ID])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)
    try:
        db.insert_artist_weekly(week=week, artist_popularity=row[COL_ARTIST_POP], artist_followers=row[COL_ARTIST_FOLLOWERS], artist_id=row[COL_ARTIST_ID])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)

    #---------------------------------------------

    # Distinct tracks in order to prevent collisions
    if row[COL_TRACK_ID] not in track_ids:

        # Handling data with empty track name (check images empty_data_all.png)
        if row[COL_TRACK_NAME] == "":
            row[COL_TRACK_NAME] = None

        collab = True if row[COL_COLLAB] == "TRUE" else False
        explicit = True if row[COL_EXPLICIT] == "TRUE" else False

        # Insert track
        db.insert_track(track_id=row[COL_TRACK_ID], track_name=row[COL_TRACK_NAME], track_number=row[COL_TRACK_NUM], collab=collab, explicit=explicit)
        
        # Insert track features
        for i in range(len(features)):
            col_feature = row[COL_DANCEABILITY + i] # Adding feature id to danceability column number will give desired feature column number
            db.insert_track_feature(track_id=row[COL_TRACK_ID], feature_id=i, value=col_feature)
        
        track_ids.append(row[COL_TRACK_ID])

    #---------------------------------------------

    # Distinct albums in order to prevent collisions and optimize blob conversions
    if row[COL_ALBUM_ID] not in album_ids:

        # Handling data with empty album name (check images empty_data_all.png)
        if row[COL_ALBUM_NAME] == "":
            row[COL_ALBUM_NAME] = None
            row[COL_ALBUM_IMG] = None
            row[COL_ALBUM_LABEL] = None

        # Convert image to blob
        album_image = None
        if row[COL_ALBUM_IMG] != None:
            album_image = url_to_blob(row[COL_ALBUM_IMG])

        # Insert album
        db.insert_album(album_id=row[COL_ALBUM_ID], album_name=row[COL_ALBUM_NAME], album_image=album_image, album_type=row[COL_ALBUM_TYPE], album_label=row[COL_ALBUM_LABEL], album_track_number=row[COL_ALBUM_TRACK_NUM])

        album_ids.append(row[COL_ALBUM_ID])

    #---------------------------------------------

    # Distinct artists in order to prevent collisions
    if row[COL_ARTIST_ID] not in artist_ids:

        # Get last 40 characters (unique) of image url as image url
        artist_image_url = row[COL_ARTIST_IMG][-40:]

        # Insert artist
        db.insert_artist(artist_id=row[COL_ARTIST_ID], artist_name=row[COL_ARTIST_NAME], artist_image_url=artist_image_url)

        # Insert artist genres if artist genres not empty
        if row[COL_ARTIST_GENRES] != "":
            for genre_id, genre_name in enumerate(genres):

                artist_genres = str_to_list(row[COL_ARTIST_GENRES])

                if genre_name in artist_genres:
                    db.insert_artist_genre(artist_id=row[COL_ARTIST_ID], genre_id=genre_id)

        artist_ids.append(row[COL_ARTIST_ID])

    #---------------------------------------------

    # Connection of track - album - artist

    # Insert exists on table ~~ track - album
    try:
        db.insert_exists_on(track_id=row[COL_TRACK_ID], album_id=row[COL_ALBUM_ID])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)

    # Insert appears on table ~~ album - artist
    try:
        db.insert_appears_on(row[COL_ALBUM_ID], row[COL_ARTIST_ID])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)

    # Insert creator table ~~ alnum - artist
    try:
        if row[COL_PIVOT] == "0":
            create_date = date_to_str(row[COL_RELEASE_DATE])
            db.insert_creator(album_id=row[COL_ALBUM_ID], create_date=create_date, artist_id=row[COL_ARTIST_ID])
    except mysql.connector.errors.IntegrityError as ex:
        # Skip primary key errors
        if ex.errno != 1062:
            print("error:", ex)

# Close database connection
db.close()