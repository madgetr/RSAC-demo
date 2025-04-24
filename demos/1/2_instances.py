import pickle
import pickletools


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


friend = Student("Alice", 25, [Course("English")])
student = Student("John", 30, [Course("Math"), Course("Science")], [friend])

with open("student_pickle.pkl", "wb") as f:
    pickle.dump(student, f)

# This will crash because the student is not JSON serializable
# with open("student_json.json", "w") as f:
#     json.dump(student, f)

input("Press Enter to load the pickle file and compare the objects")

with open("student_pickle.pkl", "rb") as f:
    student_from_pickle = pickle.load(f)

print("Student from pickle:", student_from_pickle)
print("Student == Student from pickle:", student == student_from_pickle)

input("Press Enter to disassemble the pickle file")
pickletools.dis(open("student_pickle.pkl", "rb").read())

print("""
notice STACK_GLOBAL
It is a security issue because it allows the unpickling process to access global variables and functions, 
which can lead to arbitrary code execution if the pickle data is malicious. 
This is why you should never unpickle data from an untrusted source.""")
