import os
import shutil

# --- configure these ---
source_folder = r"../dataset/filtered_baybayin-symbols_dataset"        # flat folder with all files
dest_root     = r"../dataset/baybayin-symbols (upscled and binarized)"     # where syllable folders will be created
copy_instead_of_move = True                         # set to False to move instead of copy
# -----------------------

VOWELS = set("aeiouAEIOU")
IMG_EXTS = ('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')

os.makedirs(dest_root, exist_ok=True)

def first_syllable(code: str) -> str:
    """
    Extract the first syllable:
      - V → that vowel (e.g., 'a...')
      - CV → consonant + vowel (e.g., 'ba...')
      - else → first letter only (e.g., 'bX...' -> 'b')
    """
    if not code:
        return "misc"
    c0 = code[0]
    if not c0.isalpha():
        return "misc"
    if c0 in VOWELS:
        return c0.lower()
    # consonant
    if len(code) >= 2 and code[1] in VOWELS:
        return (c0 + code[1]).lower()
    return c0.lower()

def base_code(fname: str) -> str:
    """
    Take the part before the first '-' (e.g., 'baBlbF-James.jpg' -> 'baBlbF').
    """
    return fname.split('-', 1)[0]

# Gather all files
all_files = os.listdir(source_folder)

# We’ll process every file (images and .gt.txt). This handles cases where pairs are missing.
for fname in all_files:
    if not (fname.endswith(".gt.txt") or fname.lower().endswith(IMG_EXTS)):
        continue

    code = base_code(fname)
    syll = first_syllable(code)
    dest_folder = os.path.join(dest_root, syll)
    os.makedirs(dest_folder, exist_ok=True)

    src = os.path.join(source_folder, fname)
    dst = os.path.join(dest_folder, fname)

    if copy_instead_of_move:
        shutil.copy2(src, dst)
    else:
        shutil.move(src, dst)

    print(f"{'Copied' if copy_instead_of_move else 'Moved'} {fname} -> {syll}/")

print("\n✅ Done. Files are organized by first syllable.")
