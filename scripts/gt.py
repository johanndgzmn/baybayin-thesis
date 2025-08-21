# Creates a ground truth text file in a folder. Edit lines 6, 9, and 23 (25 is optional)
import os
import shutil

# Set the path to your image folder
image_folder = '../dataset/baybayin-symbols/ngengi'

# Set the path to the folder where the text files will be saved (same as image folder in this case)
text_file_folder = '../dataset/baybayin-symbols/ngengi'  # Change this if you want a different folder for text files

# Iterate over all files in the image folder
for filename in os.listdir(image_folder):
    # Check if the file is an image (you can modify the extension check as needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        # Generate the corresponding text file name
        text_filename = os.path.splitext(filename)[0] + '.gt.txt'
        
        # Create the full path for the new text file
        text_file_path = os.path.join(text_file_folder, text_filename)
        
        # Write the letter 'a' to the text file
        with open(text_file_path, 'w', encoding="utf-8") as f:
            f.write('nge')

        print(f"Created text file: {text_filename} with content 'nge'")

print("Process complete!")
