#Tyler Seppala
#2297817
#seppala@chapman.edu
#CPSC 408-01
#Assignment 2

#This is the choices class, which contains all the logic that goes with the available choices (besides search)

import sqlite3
import pandas as pd
from pandas import DataFrame
from Students import Student
from Search import Search

#Contains all user choices except for search (it has its own class)
class Choices:
    def __init__(self):
        # access database
        self.conn = sqlite3.connect('C:\\Users\\Tyler\\PycharmProjects\\Foobar2\\Foobar2.sqlite')
        self.c = self.conn.cursor()

    def addStudent(self):
        first_name = input("What is the student's first name? ")
        last_name = input("What is the student's last name? ")
        major = input("What is the student's major? ")
        while True:
            gpa = input("What is the student's GPA? ")
            try:
                val = float(gpa) #check for propper GPA input
                break
            except ValueError:
                print("Input Invalid")
        faculty_advisor = input("Who is the student's faculty advisor? ")
        is_deleted = 0 #initialize is_deleted to false

        new_stu = Student(first_name, last_name, major, gpa, faculty_advisor, is_deleted)
        self.c.execute(
            "INSERT INTO Student('FirstName', 'LastName', 'Major', 'GPA', 'facultyAdvisor', 'isDeleted')" "VALUES (?,?,?,?,?,?)",
            new_stu.getStudent())

        # commit changes
        self.conn.commit()
        studentId = self.c.lastrowid
        print("record created", studentId)

    def update(self):
        id_num = input("What is the student's ID number? ")
        category = input("Would you like to update the student's major, or advisor (m or a)? ")
        if category == 'm': #update major
            new_major = input("What major will the student be switching to? ")
            self.c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (new_major, id_num,))
        elif category == 'a': #update advisor
            new_advisor = input("What is the name of the student's new advisor? ")
            self.c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (new_advisor, id_num,))
        else:
            print("Input invalid.")
            return
        self.conn.commit() #commit changes
        print("Student updated.")

    def delete(self):
        id_num = input("What is the student's ID number? ")
        self.c.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1, id_num,))
        self.conn.commit() #commit changes
        print("Student Deleted")

    def viewAll(self):
        self.c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE isDeleted = 0')
        all_rows = self.c.fetchall() #return all rows from the select statement
        df = DataFrame(all_rows,
                       columns=['StudentId', 'FirstName', 'LastName', 'Major', 'GPA', 'FacultyAdvisor'])
        print()
        print(df)
        print("------------------------------------------------------------------")
        print()