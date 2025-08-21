import os

# Folder containing the images
folder = "./"

# Supported image extensions
valid_extensions = (".jpg", ".jpeg", ".png", ".tiff", ".bmp")

# Loop through image files
for filename in os.listdir(folder):
    if filename.lower().endswith(valid_extensions):
        # Remove the extension
        name_without_ext = os.path.splitext(filename)[0]

        # Split at the first space
        parts = name_without_ext.split(" ", 1)

        if len(parts) == 2:
            word = parts[1].lower()
            gt_filename = f"{name_without_ext}.gt.txt"
            gt_path = os.path.join(folder, gt_filename)

            with open(gt_path, "w", encoding="utf-8") as f:
                f.write(word)

            print(f"Created: {gt_filename}")
        else:
            print(f"Skipping invalid filename: {filename}")
