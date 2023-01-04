import mysql.connector

class Database:
    connection = None
    cursor = None

    def __init__(self, args):
        self.connection = mysql.connector.connect(host=args.host, database=args.database, user=args.user, password=args.password)
        self.cursor = self.connection.cursor()

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
        query = "INSERT IGNORE INTO track(track_id, track_name, track_number, collab, explicit) VALUES (%s, %s, %s, %s, %s)"

        self.cursor.execute(query, (track_id, track_name, track_number, collab, explicit))
        self.connection.commit()

    def insert_track_weekly(self, week : str, rank : int, streams : int, track_id : str, track_popularity : int):
        query = "INSERT IGNORE INTO weekly_track VALUES (%s, %s, %s, %s, %s)"

        self.cursor.execute(query, (week, rank, streams, track_id, track_popularity))
        self.connection.commit()

    def insert_track_feature(self, track_id : str, feature_id : int, value : float):
        query = "INSERT IGNORE INTO track_features(track_id, feature_id, value) VALUES (%s, %s, %s)"

        self.cursor.execute(query, (track_id, feature_id, value))
        self.connection.commit()

    def insert_track_feature_metric(self, feature_id : int, feature_name : str):
        query = "INSERT IGNORE INTO track_feature_metrics(feature_id, feature_name) VALUES (%s, %s)"

        self.cursor.execute(query, (feature_id, feature_name))
        self.connection.commit()

    def insert_exists_on(self, track_id : str, album_id : str):
        query = "INSERT IGNORE INTO exists_on VALUES (%s, %s)"

        self.cursor.execute(query, (track_id, album_id))
        self.connection.commit()

    def insert_album(self, album_id : str, album_name : str, album_image : bytes, album_type : str, album_label : str, album_track_number : int):
        query = "INSERT IGNORE INTO album VALUES (%s, %s, %s, %s, %s, %s)"

        self.cursor.execute(query, (album_id, album_name, album_image, album_type, album_label, album_track_number))
        self.connection.commit()

    def insert_album_weekly(self, week : str, album_popularity : int, album_id : str):
        query = "INSERT IGNORE INTO weekly_album VALUES (%s, %s, %s)"

        self.cursor.execute(query, (week, album_popularity, album_id))
        self.connection.commit()

    def insert_creator():
        pass
    def insert_appears_on():
        pass
    def insert_artist():
        pass
    def insert_artist_weekly():
        pass
    def insert_artist_genre():
        pass
    
    def insert_artist_genre_metric(self, genre_id : int, genre_name : str):
        query = "INSERT IGNORE INTO artist_genre_metrics(genre_id, genre_name) VALUES (%s, %s)"

        self.cursor.execute(query, (genre_id, genre_name))
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()