import csv
import argparse
from dataset import *
from converter import *
from database import Database

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="root")
parser.add_argument("--password", default="password")
parser.add_argument("--path", default="spotify_dataset_100.csv")
args = parser.parse_args()

# Initialize the database
db = Database(args)

# Read csv file excluding column names
rows = None
with open(args.path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    rows = [row for row in csv_reader][1:]

# Load already existing artists in the database
artist_ids = db.get_artist_ids()

# Load genre list from the database
genres = db.get_genres()

# Iterate through rows in order to do insertions
for row in rows:

    # Insert weekly artist whether that artist located in artist table or not
    week = week_to_str(row[COL_WEEK])
    db.insert_artist_weekly(week=week, artist_popularity=row[COL_ARTIST_POP], artist_followers=row[COL_ARTIST_FOLLOWERS], artist_id=row[COL_ARTIST_ID])

    if row[COL_ARTIST_ID] not in artist_ids:

        # Insert distinct artists into the artist table
        artist_image_url = row[COL_ARTIST_IMG][-40:] # Since only last 40 characters of the image url is unique
        db.insert_artist(artist_id=row[COL_ARTIST_ID], artist_name=row[COL_ARTIST_NAME], artist_image_url=artist_image_url)

        # Insert creator table if the artist has pivot as 0 whcih means creator of the album
        if row[COL_PIVOT] == "0":
            create_date = week_to_str(row[COL_RELEASE_DATE])
            db.insert_creator(album_id=row[COL_ALBUM_ID], create_date=create_date, artist_id=row[COL_ARTIST_ID])

        # Insert artist genres if artist genres not empty
        if row[COL_ARTIST_GENRES] != "":
            for genre_id, genre_name in genres:

                artist_genres = str_to_list(row[COL_ARTIST_GENRES])

                if genre_name in artist_genres:
                    db.insert_artist_genre(artist_id=row[COL_ARTIST_ID], genre_id=genre_id)
        
        artist_ids.append(row[COL_ARTIST_ID])

        print("inserted", row[COL_ARTIST_NAME])
    
    # Insert appears_on table for all entries in order to connect artist with album
    db.insert_appears_on(album_id=row[COL_ALBUM_ID], artist_id=row[COL_ARTIST_ID])

# Close session
db.close()