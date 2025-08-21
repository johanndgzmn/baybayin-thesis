import os
from PIL import Image

# 🔹 Set your dataset folder here
input_folder = r"../dataset/filtered_baybayin-symbols"  # Change this to your dataset folder
output_folder = r"../dataset/filtered_baybayin-symbols/upscale"

# 🔹 Set target size (e.g., 64x64 or 128x128)
target_size = (128, 128)

# Make output folder if not exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("L")  # convert to grayscale (optional)

        # Upscale with NEAREST to preserve sharp edges of glyphs
        img_resized = img.resize(target_size, Image.NEAREST)

        # Save to output folder
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

        print(f"Upscaled: {filename} -> {target_size}")
