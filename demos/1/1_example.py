import json
import pickle
import pickletools

student = {
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
}

with open("student_pickle.pkl", "wb") as f:
    pickle.dump(student, f)

with open("student_json.json", "w") as f:
    json.dump(student, f)

with open("student_pickle.pkl", "rb") as f:
    student_from_pickle = pickle.load(f)

with open("student_json.json", "r") as f:
    student_from_json = json.load(f)

print("Student from pickle:", student_from_pickle)
print("Student == Student from pickle:", student == student_from_pickle)
print("Student from json:", student_from_json)
print("Pickle bytes:", pickle.dumps(student))

input("Press Enter to disassemble the pickle file")
pickletools.dis(pickle.dumps(student))
