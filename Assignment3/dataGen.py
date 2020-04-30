# Tyler Seppala
# 2297817
# seppala@chapman.edu
# Assignment 3

"""
This program asks for the name of a csv file, and then generates random
data that corresponds to the tables within the database.
"""

from faker import Faker
import csv

fake_data = Faker()

file_name = input("Name your CSV file: ")
num = int(input("Number of tuples to generate: "))

with open(file_name, 'w', newline='') as csv_file:
    fieldnames = ['UserName', 'Name', 'Email', 'Genre', 'Region', 'SongCount', 'FollowerCount', 'FollowingCount',
                  'CollaborationCount', 'TotalPlays', 'SongName', 'SongArtist', 'SongLength', 'SongGenre',
                  'PlayCount', 'Album', 'AlbumName', 'AlbumArtist', 'AlbumLength', 'AlbumSongCount', 'ProjectName',
                  'ProjectOwner', 'ProjectFiles']
    the_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    the_writer.writeheader()
    for i in range(0, num):
        the_writer.writerow({'UserName': fake_data.word(), 'Name': fake_data.name(), 'Genre': fake_data.word(),
                             'Region': fake_data.country(), 'SongCount': fake_data.pyint(),
                             'FollowerCount': fake_data.pyint(), 'FollowingCount': fake_data.pyint(),
                             'CollaborationCount': fake_data.pyint(), 'TotalPlays': fake_data.pyint(),
                             'SongName': fake_data.word(), 'SongArtist': fake_data.name(),
                             'SongLength': fake_data.pyint(), 'SongGenre': fake_data.word(),
                             'PlayCount': fake_data.pyint(), 'Album': fake_data.word(), 'AlbumName': fake_data.word(),
                             'AlbumArtist': fake_data.name(), 'AlbumLength': fake_data.time(),
                             'AlbumSongCount': fake_data.pyint(), 'ProjectName': fake_data.word(),
                             'ProjectOwner': fake_data.name(), 'ProjectFiles': fake_data.binary(length=64),
                             'Email': fake_data.email()})

