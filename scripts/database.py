import mysql.connector

class Database:
    connection = None
    cursor = None

    def __init__(self, args):
        self.connection = mysql.connector.connect(host=args.host,  database=args.database, user=args.user, password=args.password, port=args.port)
        self.cursor = self.connection.cursor()
    
    def clear_feature_metrics(self):
        query = "DELETE FROM track_feature_metrics"
        self.cursor.execute(query)
        self.connection.commit()

    def clear_genre_metrics(self):
        query = "DELETE FROM artist_genre_metrics"
        self.cursor.execute(query)
        self.connection.commit()

    def get_artist_ids(self) -> list:
        query = "SELECT artist_id FROM artist"
        self.cursor.execute(query)
        artist_ids = [artist_id[0] for artist_id in self.cursor.fetchall()]
        
        return artist_ids

    def get_album_ids(self) -> list:
        query = "SELECT album_id FROM album"
        self.cursor.execute(query)
        album_ids = [album_id[0] for album_id in self.cursor.fetchall()]
        
        return album_ids
    
    def get_track_ids(self) -> list:
        query = "SELECT track_id FROM track"
        self.cursor.execute(query)
        track_ids = [track_id[0] for track_id in self.cursor.fetchall()]
        
        return track_ids

    def insert_track(self, track_id : str, track_name : str, track_number : int, collab : bool, explicit : bool):
        query = "INSERT INTO track(track_id, track_name, track_number, collab, explicit) VALUES (%s, %s, %s, %s, %s)"

        self.cursor.execute(query, (track_id, track_name, track_number, collab, explicit))
        self.connection.commit()

    def insert_track_weekly(self, week : str, rank : int, streams : int, track_id : str, track_popularity : int):
        query = "INSERT INTO weekly_track VALUES (%s, %s, %s, %s, %s)"

        self.cursor.execute(query, (week, rank, streams, track_id, track_popularity))
        self.connection.commit()

    def insert_track_feature(self, track_id : str, feature_id : int, value : float):
        query = "INSERT INTO track_features(track_id, feature_id, value) VALUES (%s, %s, %s)"

        self.cursor.execute(query, (track_id, feature_id, value))
        self.connection.commit()

    def insert_track_feature_metric(self, feature_id : int, feature_name : str):
        query = "INSERT INTO track_feature_metrics(feature_id, feature_name) VALUES (%s, %s)"

        self.cursor.execute(query, (feature_id, feature_name))
        self.connection.commit()

    def insert_exists_on(self, track_id : str, album_id : str):
        query = "INSERT INTO exists_on VALUES (%s, %s)"

        self.cursor.execute(query, (track_id, album_id))
        self.connection.commit()

    def insert_album(self, album_id : str, album_name : str, album_image : bytes, album_type : str, album_label : str, album_track_number : int):
        query = "INSERT INTO album VALUES (%s, %s, %s, %s, %s, %s)"

        self.cursor.execute(query, (album_id, album_name, album_image, album_type, album_label, album_track_number))
        self.connection.commit()

    def insert_album_weekly(self, week : str, album_popularity : int, album_id : str):
        query = "INSERT INTO weekly_album VALUES (%s, %s, %s)"

        self.cursor.execute(query, (week, album_popularity, album_id))
        self.connection.commit()

    def insert_creator(self, album_id : str, create_date : str, artist_id : str):
        query = "INSERT INTO creator VALUES (%s, %s, %s)"

        self.cursor.execute(query, (album_id, create_date, artist_id))
        self.connection.commit()

    def insert_appears_on(self, album_id : str, artist_id : str):
        query = "INSERT INTO appears_on VALUES (%s, %s)"

        self.cursor.execute(query, (album_id, artist_id))
        self.connection.commit()

    def insert_artist(self, artist_id : str, artist_name : str, artist_image_url : str):
        query = "INSERT INTO artist VALUES (%s, %s, %s)"

        self.cursor.execute(query, (artist_id, artist_name, artist_image_url))
        self.connection.commit()

    def insert_artist_weekly(self, week : str, artist_popularity : int, artist_followers : int, artist_id : str):
        query = "INSERT INTO weekly_artist VALUES (%s, %s, %s, %s)"

        self.cursor.execute(query, (week, artist_popularity, artist_followers, artist_id))
        self.connection.commit()

    def insert_artist_genre(self, artist_id : str, genre_id : int):
        query = "INSERT INTO artist_genres VALUES (%s, %s)"

        self.cursor.execute(query, (artist_id, genre_id))
        self.connection.commit()
    
    def insert_artist_genre_metric(self, genre_id : int, genre_name : str):
        query = "INSERT INTO artist_genre_metrics VALUES (%s, %s)"

        self.cursor.execute(query, (genre_id, genre_name))
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()