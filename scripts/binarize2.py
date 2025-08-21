import os
from PIL import Image
from kraken import binarization

# Define input and output directories
input_dir = "./"
output_dir = os.path.join(input_dir, "binarized")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp")):
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        # Perform binarization
        binarized_image = binarization.nlbin(image, low=5, high=25)

        # Preserve original file extension
        name, ext = os.path.splitext(filename)
        binarized_image_path = os.path.join(output_dir, f"{name}{ext}")

        # Save binarized image with same format
        binarized_image.save(binarized_image_path)

        print(f"Binarized image saved: {binarized_image_path}")
