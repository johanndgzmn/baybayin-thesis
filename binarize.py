from PIL import Image
from kraken import binarization

image = Image.open("./test images/ba_00072_file018.jpg")
binarized_image = binarization.nlbin(image, low=5, high=20)
binarized_image.save("test_binarized.png")