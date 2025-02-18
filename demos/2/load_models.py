import torch

# Load the simple model
model = torch.load("simple_model.pth")
print(model)

# Load the malicious model
malicious_model = torch.load("bad_model.pth")
print(malicious_model)