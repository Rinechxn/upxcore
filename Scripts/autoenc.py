import glob
import os
import subprocess
from datetime import datetime

# Define the source and target directories
source_dir = '../Audio/WAV_Formats'
target_dir = '../Audio/MP3_Format'

# Make sure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Function to convert WAV to MP3
def convert_wav_to_mp3(wav_file, mp3_file):
    command = ['lame', '-b', '320', '--resample', '48', wav_file, mp3_file]
    subprocess.run(command, check=True)

# Find all WAV files in the source directory and its subdirectories, excluding index.xml
wav_files = [f for f in glob.glob(f'{source_dir}/**/*.wav', recursive=True) if 'index' not in f]

# Convert each WAV file to MP3 if needed
for wav_file in wav_files:
    mp3_file = os.path.join(target_dir, os.path.basename(wav_file).replace('.wav', '.mp3'))
    
    # Check if MP3 file exists and compare modification times
    if not os.path.exists(mp3_file) or os.path.getmtime(wav_file) > os.path.getmtime(mp3_file):
        convert_wav_to_mp3(wav_file, mp3_file)
        print(f"Converted: {wav_file} to {mp3_file}")
    else:
        print(f"Already up to date: {mp3_file}")

print("Conversion process complete.")
