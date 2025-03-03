import pickle


class Course:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Course(name={self.name})"

    def __eq__(self, other):
        return self.name == other.name

    # This is a malicious class that executes arbitrary python code
    def __reduce__(self):
        return exec, (f"print('Bad Pickle executes arbitrary python code {self.name}')",)

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

# Does not work out of the box
# with open("student_json.json", "w") as f:
#     json.dump(student, f)

with open("student_pickle.pkl", "rb") as f:
    student_from_pickle = pickle.load(f)

print("Student from pickle:", student_from_pickle)
print("Student == Student from pickle:", student == student_from_pickle)
