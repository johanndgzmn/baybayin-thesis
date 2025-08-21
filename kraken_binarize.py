from PIL import Image
from kraken import binarization

img = Image.open("a.png")
binarized = binarization.nlbin(img)
binarized.save("test_binarized.png")
