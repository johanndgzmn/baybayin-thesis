from PIL import Image
import os

folder = "./"

for file in os.listdir(folder):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")):
        original_path = os.path.join(folder, file)

        # Convert image to grayscale
        img = Image.open(original_path).convert("L")

        # Generate new filename with .png extension
        base_name = os.path.splitext(file)[0]
        new_filename = "base_name" + ".png"
        new_path = os.path.join(folder, new_filename)

        # Save as PNG
        img.save(new_path, format="PNG")

        print(f"Converted and saved: {new_filename}")
