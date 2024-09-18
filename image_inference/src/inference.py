import os
import io
import torch
import torch.nn.functional as F

from torch.jit import ScriptModule
from torchvision import transforms
from PIL import Image


def load_model() -> ScriptModule:
    """
    Load the model from the specified directory.
    """
    # Load the model
    model = torch.jit.load("/opt/ml/model/model.pth")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return model


def predict(image_data: bytes, model: ScriptModule) -> dict:
    """
    Generate predictions for the incoming request using the model.
    """

    image_pil = Image.open(
        io.BytesIO(image_data)
    )  # Convert the image from bytes to PIL Image
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    )
    input_tensor = transform(image_pil).unsqueeze(0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_tensor = input_tensor.to(device)

    with torch.no_grad():
        inference_result = model(input_tensor)  # Get inference on image

    probabilities = F.softmax(inference_result, dim=1)

    return {
        "predicted_class": probabilities.argmax().item(),
        "probabilities": probabilities.tolist(),
    }
