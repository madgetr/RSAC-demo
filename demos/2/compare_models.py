import torch
from simple_model import SimpleModel
SimpleModel()

def load_models():
    # Load the original (simple) model
    model = torch.load("simple_model.pth")
    print("Original Model:")
    print(model)

    # Load the infected model (this will trigger the system call)
    infected_model = torch.load("infected_model.pth")
    print("infected Model:")
    print(infected_model)

if __name__ == "__main__":
    load_models()