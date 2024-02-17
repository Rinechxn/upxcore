import sqlite3
import os

# Database file
db_file = './Database/songs_database.db'

# Directories containing the song files
wav_dir = './Audio/WAV_Formats'
mp3_dir = './Audio/MP3_Format'

# Connect to SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table for storing song records
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    format TEXT NOT NULL
)
''')

# Function to insert a song record into the database
def insert_song(file_name, format):
    cursor.execute('INSERT INTO songs (file_name, format) VALUES (?, ?)', (file_name, format))
    conn.commit()

# Function to scan directories and add song files to the database
def scan_and_add(directory, format):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(format.lower()):
                insert_song(file, format)

# Scan directories and add song files to the database
scan_and_add(wav_dir, 'WAV')
scan_and_add(mp3_dir, 'MP3')

# Query and print all records to verify
cursor.execute('SELECT * FROM songs')
songs = cursor.fetchall()
for song in songs:
    print(song)

# Close the database connection
conn.close()
