import pickle

student = {
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
}

with open("good_pickle.pkl", "wb") as f:
    pickle.dump(student, f)

with open("good_pickle.pkl", "rb") as f:
    student_from_pickle = pickle.load(f)

    print("Student from pickle:", student_from_pickle)
    print("Student == Student from pickle:", student == student_from_pickle)

