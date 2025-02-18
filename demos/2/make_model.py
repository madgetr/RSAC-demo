import torch
import torch.nn as nn

# Step 1: Create and save a simple PyTorch model
def make_simple_model():
    # A simple linear model
    model = nn.Linear(2, 1)
    torch.save(model, "simple_model.pth")