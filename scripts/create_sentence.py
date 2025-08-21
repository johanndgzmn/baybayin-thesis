import os
import random
from PIL import Image

# Parameters
input_folder = "./"
output_folder = "./sentence"
num_sentences = 1000
min_words = 3
max_words = 10
target_height = 64  # Resize all word images to this height
spacer_width = 20   # Pixels of space between words

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get all image files with word names (must include a space in filename)
image_files = [
    f for f in os.listdir(input_folder)
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")) and " " in f
]

# Load images and their corresponding word labels
image_data = []
for f in image_files:
    path = os.path.join(input_folder, f)
    img = Image.open(path).convert("L")
    word = os.path.splitext(f)[0].split(" ", 1)[1].lower()
    image_data.append((img, word))

# Generate sentences
for i in range(1, num_sentences + 1):
    num_words = random.randint(min_words, max_words)
    selected = random.sample(image_data, num_words)

    resized_images = []
    sentence_text = []

    for img, word in selected:
        # Resize image to uniform height, maintaining aspect ratio
        ratio = target_height / img.height
        new_width = int(img.width * ratio)
        resized = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
        resized_images.append(resized)
        sentence_text.append(word)

    # Add space between words
    spacer = Image.new("L", (spacer_width, target_height), color=255)
    sentence_images = []
    for j, word_img in enumerate(resized_images):
        sentence_images.append(word_img)
        if j < len(resized_images) - 1:
            sentence_images.append(spacer)

    # Create a new blank image to hold the sentence
    total_width = sum(img.width for img in sentence_images)
    sentence_img = Image.new("L", (total_width, target_height), color=255)

    x_offset = 0
    for img in sentence_images:
        sentence_img.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save the image
    base_name = f"sentence_{i:04d}"
    image_path = os.path.join(output_folder, base_name + ".png")
    sentence_img.save(image_path)

    # Save the ground truth without .png in the filename
    gt_path = os.path.join(output_folder, base_name + ".gt.txt")
    with open(gt_path, "w", encoding="utf-8") as f:
        f.write(" ".join(sentence_text))

    print(f"Saved: {base_name}.png | Text: {' '.join(sentence_text)}")
