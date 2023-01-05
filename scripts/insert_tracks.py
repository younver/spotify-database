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

# Insert distinct tracks to track table
track_ids = db.get_track_ids()
for row in rows:

    # Insert weekly track whether that track located in track table or not
    week = week_to_str(row[COL_WEEK])
    db.insert_track_weekly(week=week, rank=row[COL_RANK], streams=row[COL_STREAMS], track_id=row[COL_TRACK_ID], track_popularity=row[COL_TRACK_POP])

    if row[COL_TRACK_ID] not in track_ids:
        
        # Handling data with empty track name (check images empty_data_all.png)
        if row[COL_TRACK_NAME] == "":
            row[COL_TRACK_NAME] = None

        collab = True if row[COL_COLLAB] == "TRUE" else False
        explicit = True if row[COL_EXPLICIT] == "TRUE" else False
        db.insert_track(track_id=row[COL_TRACK_ID], track_name=row[COL_TRACK_NAME], track_number=row[COL_TRACK_NUM], collab=collab, explicit=explicit)
        
        # Insert feature values to track_features table
        for i in range(len(features)):
            col_feature = row[COL_DANCEABILITY + i] # Adding feature id to danceability column number will give desired feature column number
            db.insert_track_feature(track_id=row[COL_TRACK_ID], feature_id=i, value=col_feature)
        
        track_ids.append(row[COL_TRACK_ID])

        print("inserted", row[COL_TRACK_NAME])

# Close session
db.close()