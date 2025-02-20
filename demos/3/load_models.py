import torch


def load_models():
    # Load the original (simple) model
    print("Loading Original Model")
    torch.load("diffusion_pytorch_model.bin")
    print("Done.")
    # Load the infected model (this will trigger the pip install of a malicious pypi package)
    print("Loading infected Model")
    torch.load("infected_model.bin")
    print("Done.")

if __name__ == "__main__":
    load_models()