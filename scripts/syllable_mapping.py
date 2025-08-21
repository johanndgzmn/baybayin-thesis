import os

# Folder containing the .txt files
folder = "../dataset/images_word/binarized/"

# Syllable mapping
syllable_map = {
    'bi': 'be', 'bu': 'bo', 'ra': 'da', 'di': 'de', 'du': 'do',
    'e': 'i', 'gi': 'ge', 'gu': 'go', 'hi': 'he', 'hu': 'ho',
    'ki': 'ke', 'ku': 'ko', 'li': 'le', 'lu': 'lo', 'mi': 'me',
    'mu': 'mo', 'ni': 'ne', 'nge': 'ngi', 'ngu': 'ngo', 'nu': 'no',
    'u': 'o', 'pi': 'pe', 'pu': 'po', 'ri': 're', 'ru': 'ro',
    'si': 'se', 'su': 'so', 'ti': 'te', 'tu': 'to',
    'wi': 'we', 'wu': 'wo', 'yi': 'ye', 'yu': 'yo'
}

# Sort the keys by descending length to avoid partial replacements (e.g. 'gi' before 'g')
replacement_order = sorted(syllable_map.keys(), key=lambda x: -len(x))

# Apply replacements
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # Apply syllable replacements
        for old in replacement_order:
            content = content.replace(old, syllable_map[old])

        # Overwrite the file with updated content
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Updated: {filename}")
