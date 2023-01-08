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

# Read csv file excluding column names
rows = None
with open(args.path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    rows = [row for row in csv_reader][1:]

for row in rows:

    week = week_to_str(row[COL_WEEK])


    db.insert_track_weekly(week=week, rank=row[COL_RANK], streams=row[COL_STREAMS], track_id=row[COL_TRACK_ID], track_popularity=row[COL_TRACK_POP])
    db.insert_album_weekly(week=week, album_popularity=row[COL_ALBUM_POP], album_id=row[COL_ALBUM_ID])
    db.insert_artist_weekly(week=week, artist_popularity=row[COL_ARTIST_POP], artist_followers=row[COL_ARTIST_FOLLOWERS], artist_id=row[COL_ARTIST_ID])

# Close session
db.close()