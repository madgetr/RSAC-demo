import pickle

student = {
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
}

with open("good_pickle.pkl", "wb") as f:
    pickle.dump(student, f)
