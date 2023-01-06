import argparse
from dataset import *
from converter import *
from database import Database

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

# Select first 5 album image
query = "SELECT album_img FROM album LIMIT 5"
db.cursor.execute(query)
blob_images = db.cursor.fetchall()

# Display images
for blob_image in blob_images:
    blob_image = blob_image[0]

    image = blob_to_image(blob_image)
    image.show()
