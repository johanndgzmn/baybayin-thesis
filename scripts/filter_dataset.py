# Filters dataset to 100 images per character
# import os
# import shutil

# # Set the path to your source folder containing images and ground truth text files
# source_folder = '../dataset/baybayin-symbols/dara'  # Change as needed

# # Set the path to the filtered_dataset folder
# filtered_dataset_folder = '../dataset/filtered_baybayin-symbols'
# filtered_images_folder = os.path.join(filtered_dataset_folder, 'images')
# filtered_gt_folder = os.path.join(filtered_dataset_folder, 'gt')

# # Create filtered_dataset/images and filtered_dataset/gt if they don't exist
# os.makedirs(filtered_images_folder, exist_ok=True)
# os.makedirs(filtered_gt_folder, exist_ok=True)

# # Get all image files and ground truth text files
# image_exts = ('.png', '.jpg', '.jpeg', '.bmp')
# image_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith(image_exts)])
# gt_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith('.gt.txt')])

# # Take the first 100 of each
# selected_images = image_files[:50]
# selected_gt = gt_files[:50]

# # Copy images
# for filename in selected_images:
#     src = os.path.join(source_folder, filename)
#     dst = os.path.join(filtered_images_folder, filename)
#     shutil.copy2(src, dst)
#     print(f"Copied image: {filename}")

# # Copy ground truth text files
# for filename in selected_gt:
#     src = os.path.join(source_folder, filename)
#     dst = os.path.join(filtered_gt_folder, filename)
#     shutil.copy2(src, dst)
#     print(f"Copied ground truth: {filename}")

# print("Filtering and copying complete!")
# Filters dataset to 50 images per character (change as needed)
# ------------------------------------------------------------------------
import os
import shutil

# Path to your source root folder (contains subfolders for each character)
source_root = '../dataset/baybayin-symbols'

# Path to filtered_dataset
filtered_dataset_folder = '../dataset/filtered_baybayin-symbols'
filtered_images_folder = os.path.join(filtered_dataset_folder, 'images')
filtered_gt_folder = os.path.join(filtered_dataset_folder, 'gt')

# Create filtered_dataset/images and filtered_dataset/gt if they don't exist
os.makedirs(filtered_images_folder, exist_ok=True)
os.makedirs(filtered_gt_folder, exist_ok=True)

# Extensions for images
image_exts = ('.png', '.jpg', '.jpeg', '.bmp')

# Loop through all subfolders (characters)
for character_folder in os.listdir(source_root):
    char_path = os.path.join(source_root, character_folder)

    if not os.path.isdir(char_path):
        continue  # skip non-folder files

    print(f"\nProcessing folder: {character_folder}")

    # Get all image and gt files for this character
    image_files = sorted([f for f in os.listdir(char_path) if f.lower().endswith(image_exts)])
    gt_files = sorted([f for f in os.listdir(char_path) if f.lower().endswith('.gt.txt')])

    # Take the first 50 (adjust as needed)
    selected_images = image_files[:50]
    selected_gt = gt_files[:50]

    # Copy images
    for filename in selected_images:
        src = os.path.join(char_path, filename)
        dst = os.path.join(filtered_images_folder, f"{character_folder}_{filename}")
        shutil.copy2(src, dst)
        print(f"Copied image: {filename} -> {dst}")

    # Copy ground truth files
    for filename in selected_gt:
        src = os.path.join(char_path, filename)
        dst = os.path.join(filtered_gt_folder, f"{character_folder}_{filename}")
        shutil.copy2(src, dst)
        print(f"Copied ground truth: {filename} -> {dst}")

print("\nFiltering and copying complete!")
