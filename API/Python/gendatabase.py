import sqlite3
import os
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from datetime import timedelta

# Database file
db_file = './Database/songs_database.db'

# Directories containing the song files
wav_dir = './Audio/WAV_Formats'
mp3_dir = './Audio/MP3_Format'

# Connect to SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create tables for WAV and MP3 songs with a format column
cursor.execute('''
CREATE TABLE IF NOT EXISTS song_wav (
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    format TEXT NOT NULL,
    size TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS song_mp3 (
    id INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    format TEXT NOT NULL,
    size TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')

# Function to insert a song record into the respective database table
def insert_song(file_name, file_path, format, size, duration):
    if format.lower() == 'wav':
        cursor.execute('INSERT INTO song_wav (file_name, file_path, format, size, duration) VALUES (?, ?, ?, ?, ?)', (file_name, file_path, format.upper(), size, duration))
    elif format.lower() == 'mp3':
        cursor.execute('INSERT INTO song_mp3 (file_name, file_path, format, size, duration) VALUES (?, ?, ?, ?, ?)', (file_name, file_path, format.upper(), size, duration))
    conn.commit()

# Function to get the duration of a song file and convert it to HH:MM:SS
def get_duration(file_path, format):
    try:
        if format.lower() == 'mp3':
            audio = MP3(file_path)
        elif format.lower() == 'wav':
            audio = WAVE(file_path)
        else:
            return "00:00:00"  # Unsupported format
        duration_seconds = int(audio.info.length)
        duration_formatted = str(timedelta(seconds=duration_seconds))
        return duration_formatted
    except Exception as e:
        print(f"Error getting duration for {file_path}: {e}")
        return "00:00:00"

# Function to get file size in a readable format (e.g., KB, MB)
def get_file_size(file_path):
    size_bytes = os.path.getsize(file_path)
    return f"{size_bytes}"
    # size_kb = size_bytes / 1024
    # if size_kb > 1024:
    #     return f"{size_kb / 1024:.2f} MB"
    # else:
    #     return f"{size_kb:.2f} KB"

# Function to scan directories and add song files to the respective database table
def scan_and_add(directory, format):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.' + format.lower()):
                file_path = os.path.join(root, file)
                duration = get_duration(file_path, format)
                size = get_file_size(file_path)
                path = file_path
                insert_song(file, path, format, size, duration)

# Scan directories and add song files to the database
scan_and_add(wav_dir, 'WAV')
scan_and_add(mp3_dir, 'MP3')

# Close the database connection
conn.close()
