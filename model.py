import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    """Generate a caption for a given image."""
    image = Image.open(image_path).convert("RGB")  # Open image
    inputs = processor(images=image, return_tensors="pt")  # Preprocess image

    with torch.no_grad():
        output = model.generate(**inputs)  # Generate caption

    caption = processor.decode(output[0], skip_special_tokens=True)  # Decode result
    return caption

