from dataset import *
from database import Database
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--port", default=3306)
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="admin")
parser.add_argument("--password", default="")
parser.add_argument("--path", default="../datasets/spotify_dataset_100.csv")
args = parser.parse_args()

# Initialize the database
db = Database(args)

# Insert features into the table
for i in range(len(features)):
    feature = features[i]
    db.insert_track_feature_metric(feature_id = i, feature_name = feature)
    print("inserted", feature)

# Close session
db.close()