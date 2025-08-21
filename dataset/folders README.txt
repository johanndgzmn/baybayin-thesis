baybayin_word_dataset_v2 --> contains words with ground truth text. characters with multiple meanings (po/pu) are generalized to a single ground truth (e.g. po)
baybayin-symbols (original) --> original baybayin symbols with diacritics. not upscaled and binarized.
baybayin-symbols (upscaled and binarized) --> baybayin-symbols (original) folder. upscaled to 128x128 and binarized.
filtered_baybayin-symbols --> baybayin-symbols (upscaled and binarized) folder but filtered to 50 images per character
filtered_baybayin-symbols_dataset --> baybayin-symbols (upscaled and binarized) folder but filtered to 100 images per character
filtered_dataset_latin --> binarized baybayin symbols without diacritics and with ground truth text file. 50 images per character.
images_(latin ground truth) --> baybayin symbols without diacritics (ALL files, non-filtered) (OLD DATASET)
images_sentence --> images_word but combined into sentences
images_word --> original baybayin words



tldr:
use filtered_baybayin-symbols for training characters. or if possible use filtered_baybayin-symbols_dataset
once a good accuracy is obtained, proceed to baybayin_word_dataset_v2
then images_sentence

