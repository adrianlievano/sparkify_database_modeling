# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS songplays"""
user_table_drop = """DROP TABLE IF EXISTS users"""
song_table_drop = """DROP TABLE IF EXISTS songs"""
artist_table_drop = """DROP TABLE IF EXISTS artists"""
time_table_drop = """DROP TABLE IF EXISTS time"""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, artist_location varchar, user_agent varchar);""")
                         

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude numeric, artist_longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (hour int, day int, week int, month int, year int, weekday_name varchar);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, artist_location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)\
VALUES (%s, %s, %s, %s, %s);""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)\
VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s);""")

time_table_insert = ("""INSERT INTO time (hour, day, week, month, year, weekday_name)\
VALUES (%s, %s, %s, %s, %s, %s);""")

# FIND SONGS
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.

song_select = ("""SELECT songs.song_id, songs.artist_id FROM songs JOIN artists 
ON songs.artist_id = artists.artist_id 
WHERE (songs.title = %s AND artists.artist_name = %s AND songs.duration = %s)
""")

#song_select = ("""SELECT song_id, artists.artist_id FROM songs,    
       #           artists WHERE (songs.title = %s 
       #           AND artists.name = %s AND songs.duration = %s)
       #        """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]