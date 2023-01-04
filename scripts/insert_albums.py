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

# Insert distinct albums to album table
album_ids = db.get_album_ids()
for row in rows:

    if row[COL_ALBUM_ID] not in album_ids:
        album_image = url_to_blob(row[COL_ALBUM_IMG])
        db.insert_album(album_id=row[COL_ALBUM_ID], album_name=row[COL_ALBUM_NAME], album_image=album_image, album_type=row[COL_ALBUM_TYPE], album_label=row[COL_ALBUM_LABEL], album_track_number=row[COL_ALBUM_TRACK_NUM])
        
        # Insert weekly album
        week = week_to_str(row[COL_WEEK])
        db.insert_album_weekly(week=week, album_popularity=row[COL_ALBUM_POP], album_id=row[COL_ALBUM_ID])

        album_ids.append(row[COL_ALBUM_ID])

        print("inserted", row[COL_ALBUM_NAME])

    # Insert exists_on table for all entries in order to connect album with track
    # Since we used ignore keyword in insertion query, no collisions exists
    db.insert_exists_on(track_id=row[COL_TRACK_ID], album_id=row[COL_ALBUM_ID])

# Close session
db.close()