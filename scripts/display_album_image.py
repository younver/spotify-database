import argparse
from dataset import *
from converter import *
from database import Database

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="root")
parser.add_argument("--password", default="1q2we3")
parser.add_argument("--path", default="spotify_dataset_100.csv")
args = parser.parse_args()

# Initialize the database
db = Database(args)

query = "SELECT * FROM artist_genre_metrics"
db.cursor.execute(query)
genres = [[genre[0], genre[1]] for genre in db.cursor.fetchall()]

for genre_id, genre_name in genres:
    print(genre_id, genre_name)
    break

# Select first 5 album image
query = "SELECT album_img FROM album LIMIT 5"
db.cursor.execute(query)
blob_images = db.cursor.fetchall()

# Display images
for blob_image in blob_images:
    blob_image = blob_image[0]

    image = blob_to_image(blob_image)
    image.show()
