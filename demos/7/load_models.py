import torch


def load_models():
    # Load the original (simple) model
    torch.load("malicious_model.pth")


if __name__ == "__main__":
    load_models()