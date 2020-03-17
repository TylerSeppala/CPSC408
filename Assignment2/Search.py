#Tyler Seppala
#2297817
#seppala@chapman.edu
#CPSC 408-01
#Assignment 2

#This is the search class, which provides all the logic needed to search the database

import sqlite3
import pandas as pd
from pandas import DataFrame
from Students import Student

class Search:
    def __init__(self):
        conn = sqlite3.connect('C:\\Users\\Tyler\\PycharmProjects\\Foobar2\\Foobar2.sqlite')
        self.c = conn.cursor()

    def searchByMajor(self, input_param):
        self.c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE Major = ? AND isDeleted = 0', input_param)
        self.printSearchResults()

    def searchByGpa(self, input_param):
        self.c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE GPA = ? AND isDeleted = 0', input_param)
        self.printSearchResults()

    def searchByAdvisor(self, input_param):
        self.c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE FacultyAdvisor = ? AND isDeleted = 0', input_param)
        self.printSearchResults()

    def printSearchResults(self):
        all_rows = self.c.fetchall()
        df = DataFrame(all_rows, columns=['StudentId', 'FirstName', 'LastName', 'Major', 'GPA', 'FacultyAdvisor'])
        print()
        print(df)
        print("------------------------------------------------------------------")
        print()