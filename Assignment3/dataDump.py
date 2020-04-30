# Tyler Seppala
# 2297817
# seppala@chapman.edu
# Assignment 3

"""
This program asks for the name of a csv file, and then dumps its contents
into the corresponding tables in a database.
"""

import mysql.connector
import csv

db = mysql.connector.connect(
    host="35.233.148.205",
    user="root",
    passwd="Bluez123!",
    database="Assignment3"
)

file_name = input("What is the name of your data file (.csv): ")
my_cursor = db.cursor()

with open(file_name, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    counter = 0
    for line in csv_reader:
        #counter += 1
        my_cursor.execute("INSERT INTO Users(UserName, Name, Email, Genre, Region)" "VALUES (%s, %s, %s, %s, %s)",
                          (line[0], line[1], line[2], line[3], line[4]))
        last_id = my_cursor.lastrowid
        my_cursor.execute("INSERT INTO UserStats(UserId, SongCount, FollowerCount, FollowingCount, CollaborationCount, TotalPlays)" "VALUES (%s, %s, %s, %s, %s, %s)",
                          (last_id, line[5], line[6], line[7], line[8], line[9]))
        my_cursor.execute("INSERT INTO Albums(AlbumName, Artist, ArtistId, AlbumLength, SongCount)" "VALUES (%s, %s, %s, %s, %s)",
                          (line[16], line[17], last_id, line[18], line[19]))
        last_album = my_cursor.lastrowid
        my_cursor.execute("INSERT INTO Songs(SongName, SongArtist, ArtistId, SongLength, Genre, PlayCount, Album, AlbumId)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                          (line[10], line[11], last_id, line[12], line[13], line[14], line[15], last_album))
        my_cursor.execute("INSERT INTO Projects(ProjectName, ProjectOwner, OwnerId, ProjectFiles)" "VALUES (%s, %s, %s, %s)",
                          (line[20], line[21], last_id, line[22]))

db.commit()


db.close()
