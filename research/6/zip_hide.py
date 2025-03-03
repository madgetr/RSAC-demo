import zipFile

zip_file = "malicious_model.pth"

temp_zip = "temp.pth"

# Create a new ZIP file without "malicious_model/data.pkl"
with zipFile.ZipFile(zip_file, 'r') as archive:
    with zipFile.ZipFile(temp_zip, 'w', zipFile.ZIP_DEFLATED) as new_archive:
        for item in archive.infolist():
            new_archive.writestr(item, archive.read(item.filename))  # Copy all but "data.pkl"


# Verify removal
with zipFile.ZipFile(temp_zip, 'r') as archive:
    print(archive.namelist())
    print(archive.read("malicious_model/data.pkl"))  # Verify "data.pkl" is gone

import torch
# torch.load(temp_zip)  # Load the cleaned model