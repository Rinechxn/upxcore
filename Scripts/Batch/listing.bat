@echo off
cd %~dp0
ECHO ------------------------------------------------
del Database\songs_database.db
python Scripts\autoenc.py
python gendatabase.py
python Scripts\version.py
scp -P 191 Database/songs_database.db reds@devilgirls44.ddns.net:~/nxsongdatabase/Database 
ECHO ------------------------------------------------
pause