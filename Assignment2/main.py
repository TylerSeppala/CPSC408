#Tyler Seppala
#2297817
#seppala@chapman.edu
#CPSC 408-01
#Assignment 2

#This program provides user prompts which access a database of student information.
#Users can add students, search students, update students, delete students, and view all students.

import sqlite3
import pandas as pd
from pandas import DataFrame
from Students import Student
from Search import Search
from Choices import Choices

#Primary loop that presents user choices
while True:
    choice = input("What would you like to do? ('a' = add student, 's' = search student, 'u' = update student, 'd' = delete student, 'v' = view all, 'q' = quit) ")
    choices = Choices() #instance of the choices class

    #add student
    if choice == 'a':
        choices.addStudent()
        continuing = input("Continue? (y/n) ") #check if user wants to continue
        if continuing == "n":
            break

    #search for student
    elif choice == "s":
        new_search = Search() #instance of search class
        search_choice = input("What would you like to search by? ('m' = Major, 'g' = GPA, 'a' = Advisor) ")
        if search_choice.lower() == "m":
            major = input("Enter the student's major: ")
            input_param = (major,) #insert input into tuple
            new_search.searchByMajor(input_param)
        elif search_choice.lower() == "g":
            gpa = input("Enter the student's GPA: ")
            input_param = (gpa,) #insert input into tuple
            new_search.searchByGpa(input_param)
        elif search_choice.lower() == "a":
            advisor = input("Enter the name of the student's advisor: ")
            input_param = (advisor,) #insert input into tuple
            new_search.searchByAdvisor(input_param)
        else:
            print("Input invalid.")

        continuing = input("Continue? (y/n) ") #check if user wants to continue
        if continuing == "n":
            break

    #update student
    elif choice == "u":
        choices.update()
        continuing = input("Continue? (y/n) ")
        if continuing == "n":
            break

    #delete student
    elif choice == "d":
        choices.delete()
        continuing = input("Continue? (y/n) ")
        if continuing == "n":
            break

    #view all students
    elif choice == "v":
        choices.viewAll()
        continuing = input("Continue? (y/n) ")
        if continuing == "n":
            break

    #quit
    elif choice == "q":
        break

    #error check
    else:
        print("Input invalid.")