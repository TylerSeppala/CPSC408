#Tyler Seppala
#2297817
#seppala@chapman.edu
#CPSC 408-01
#Assignment 2

#This is the student class, which propperly formats data for the database.

class Student:

    def __init__(self, first_name, last_name, major, gpa, faculty_advisor, is_deleted):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.faculty_advisor = faculty_advisor
        self.is_deleted = is_deleted

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getMajor(self):
        return self.major

    def getGpa(self):
        return self.gpa

    def getFacultyAdvisor(self):
        return self.faculty_advisor

    def getIsDeleted(self):
        return self.is_deleted

    def getStudent(self):
        return (self.getFirstName(), self.getLastName(), self.getMajor(), self.getGpa(), self.getFacultyAdvisor(), self.getIsDeleted())