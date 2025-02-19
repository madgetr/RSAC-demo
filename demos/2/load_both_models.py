# Step 4: Load both the original and malicious models to demonstrate behavior

import torch

def load_models():
    # Load the original (simple) model
    model = torch.load("simple_model.pth")
    print("Original Model:")
    print(model)

    # Load the malicious model (this will trigger the exec call)
    malicious_model = torch.load("bad_model.pth")
    print("Malicious Model:")
    print(malicious_model)

if __name__ == "__main__":
    load_models()