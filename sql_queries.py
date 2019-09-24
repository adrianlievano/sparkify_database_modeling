# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS songplays"""
user_table_drop = """DROP TABLE IF EXISTS users"""
song_table_drop = """DROP TABLE IF EXISTS songs"""
artist_table_drop = """DROP TABLE IF EXISTS artists"""
time_table_drop = """DROP TABLE IF EXISTS time"""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int,\
start_time int, user_id int, level int, song_id varchar, artist_id varchar, session_id int, artist_location varchar, user_agent varchar);""")
                         

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level int);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar, artist_location varchar, artist_latitude numeric, artist_longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day int, week int, month int, year int, weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id,\
artist_id, session_id, artist_location, user_agent\
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (1, 2, 3, 4, 'asd', 'asdasd', 7, 'miami', 'xax'))

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)\
VALUES (%s, %s, %s, %s, %s)""", (1, 'Adrian', 'Lievano', 'M', 5))

song_table_insert = ("""INSERT INTO songs (song_id, title, year, duration)\
VALUES (%s, %s, %s, %s)""", ('asd', 'BOOM', 2019, 40.2))

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_location, artist_latitude, artist_longitude)\
VALUES (%s, %s, %s, %s)""", (1, 'miami', 30.22, 40.111))

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
VALUES (%s, %s, %s, %s, %s, %s, %s)""", (1, 2, 3, 4, 5, 6, 7))

# FIND SONGS

song_select = ("""select * from songs""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]