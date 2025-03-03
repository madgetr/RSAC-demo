import pickle
import pickletools


class Exploit:
    def __init__(self, student):
        self.student = student
    def __reduce__(self):
        return exec, ("print('Bad Pickle executes arbitrary python code')",), None, None, None

class Course:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Course(name={self.name})"

    def __eq__(self, other):
        return self.name == other.name

class Student:
    def __init__(self, name, age, courses=None, friends=None):
        self.name = name
        self.age = age
        self.courses = courses
        self.friends = friends if friends else []

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, courses={self.courses}, friends={self.friends})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.courses == other.courses



pickletools.dis(open("student_pickle.pkl", "rb").read())

