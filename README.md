# spotify-database

### instructions:
1. clone the repository
2. create the database as instructed in `create_database.sql`
3. install requirements with `python3 -m pip install -r requirements.txt`
4. go to scripts directory and execute `python3 insert.py` with desired parameters

### parameters for scripts
`python3 insert.py --host localhost --database spotify --user root --password cmonmanthatstooez --path ../datasets/spotify_dataset_100.csv`
* `--host` for the host of the mysql server (optional, `localhost` by default)
* `--port` for the port of the mysql server (optional, `3306` by default)
* `--database` for the database name from mysql server (optional, `spotify` by default)
* `--user` for the user of the mysql server (optional, `admin` by default)
* `--password` for the password of the user (optional, empty by default)
* `--path` for the file path of the csv dataset (optional, `../datasets/spotify_dataset_100.csv` by default)
