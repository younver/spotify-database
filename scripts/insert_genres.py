import csv
from dataset import *
from database import Database
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="root")
parser.add_argument("--password", default="password")
parser.add_argument("--path", default="spotify-top-200-dataset.csv")
args = parser.parse_args()

# Initialize the database
db = Database(args)

# Read csv file
rows = None
with open(args.path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    rows = [row for row in csv_reader]

# Find distinct genres
genres = []
for row in rows:
    artist_genres = row[COL_ARTIST_GENRES].split(',')
    
    for genre in artist_genres:
        genre = genre.strip()
        
        if genre not in genres:
            genres.append(genre)

# Insert genre metrics into the table
for i in range(len(genres)):
    genre = genres[i]
    db.insert_artist_genre_metric(genre_id = i, genre_name = genre)
    print("inserted", genre)

# Close session
db.close()