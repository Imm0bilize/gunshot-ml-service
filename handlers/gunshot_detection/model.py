import torch
import torchvision


class GunshotClassification(torch.nn.Module):
    def __init__(self):
        super(GunshotClassification, self).__init__()

        model = torchvision.models.mobilenet_v2(pretrained=False, num_classes=1)
        state_dict = torch.load("weights/mobilenetv2.pt")
        model.load_state_dict(state_dict)
        model.eval()

        self.classifier = model

    def __call__(self, x):
        x = self.classifier(x)
        return torch.sigmoid(x)


total_model = GunshotClassification()
total_model.eval()

sm = torch.jit.trace(total_model, torch.rand((1, 3, 128, 2000)))
sm.save("weights/mobilenetv2_trace.pt")
