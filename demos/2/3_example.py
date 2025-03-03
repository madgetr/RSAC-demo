import torch

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()

        self.linear1 = torch.nn.Linear(100, 200)
        self.activation = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(200, 10)
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.softmax(x)
        return x


def load_models():
    # Load the original (simple) model
    model = torch.load("simple_model.pth")
    print("Original Model:")
    print(model)

    # Load the infected model (this will trigger the system call)
    infected_model = torch.load("infected_model.pth")
    print("infected Model:")
    print(infected_model)

if __name__ == "__main__":
    load_models()