from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load pretrained BLIP model (Vision + Language model)
print("Loading model... (first time, this will download the model)")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    # Open image
    raw_image = Image.open(image_path).convert('RGB')

    # Process image for the model
    inputs = processor(raw_image, return_tensors="pt")

    # Generate caption
    output = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption

if __name__ == "__main__":
    image_path = input("Enter image path (e.g. sample.jpg): ")
    caption = generate_caption(image_path)
    print("\nGenerated Caption:", caption)