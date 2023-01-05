import argparse
import subprocess

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost")
parser.add_argument("--database", default="spotify")
parser.add_argument("--user", default="root")
parser.add_argument("--password", default="")
parser.add_argument("--path", default="../datasets/spotify_dataset_100.csv")
args = parser.parse_args()

# Insert genres
print("\n\n\n~~ inserting genres ~~")
process = subprocess.Popen(["python3", "insert_genres.py", "--host", args.host, "--database", args.database, "--user", args.user, "--password", args.password, "--path", args.path])
process.wait()

# Insert features
print("\n\n\n~~ inserting features ~~")
process = subprocess.Popen(["python3", "insert_features.py", "--host", args.host, "--database", args.database, "--user", args.user, "--password", args.password, "--path", args.path])
process.wait()

# Insert tracks
print("\n\n\n~~ inserting tracks ~~")
process = subprocess.Popen(["python3", "insert_tracks.py", "--host", args.host, "--database", args.database, "--user", args.user, "--password", args.password, "--path", args.path])
process.wait()

# Insert albums
print("\n\n\n~~ inserting albums ~~")
process = subprocess.Popen(["python3", "insert_albums.py", "--host", args.host, "--database", args.database, "--user", args.user, "--password", args.password, "--path", args.path])
process.wait()

# Insert artists
print("\n\n\n~~ inserting artists ~~")
process = subprocess.Popen(["python3", "insert_artists.py", "--host", args.host, "--database", args.database, "--user", args.user, "--password", args.password, "--path", args.path])
process.wait()