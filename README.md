## Purpose
A startup called Sparkify wants to analyze the data they collect on songs and user activitiy on their new music streaming application. The analytics team wants to understand which songs users listen most often. There is currently no easy way to query their data, which resides in a directory of JSON logs. In this repository, we create a Postgres database with tables designed to optimize queries for song play analysis. We create a database schema and an ETL processing pipeline for Sparkify.

### Database Schema & ETL Design
We designed a Star database schema that uses the following fact and dimension tables: 

#### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
<bold>data_types</bold>: (timestamp, int, varchar, varchar, varchar, int, varchar, varchar)

#### Dimension Tables
##### users - users in the app
user_id, first_name, last_name, gender, level
<bold>data_types</bold>:(int, varchar, varchar, varchar, varchar)

##### songs - songs in music database
song_id, title, artist_id, year, duration
<bold>data_types</bold>: (varchar, varchar, varchar, int, numeric)

##### artists - artists in music database
artist_id, name, location, latitude, longitude
<bold>data_types</bold>: (varchar, varchar, varchar, numeric, numeric)

##### time - timestamps of records in songplays broken down into specific units
hour, day, week, month, year, weekday
<bold>data_types</bold>: (int, int, int, int, int, varchar )

### Example Queries

In this query, we demonstrate how to join across multiple tables and select songs based on the title, artist_name, and the duration of song. 

Query: 'song_select = ("""SELECT songs.song_id, songs.artist_id FROM songs JOIN artists 
ON songs.artist_id = artists.artist_id 
WHERE (songs.title = %s AND artists.artist_name = %s AND songs.duration = %s)
""")'

