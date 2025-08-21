# Setup
1. Create a virtual environment ``` python -m venv kraken ```
2. Activate virtual environment ``` Scripts\activate```
3. Install dependencies
```
pip install kraken
pip install tensorflow
```


# Training:
Navigate to folder with all the images + ground truth text file then run
```ketos train *.png --logger tensorboard```
This outputs a console text.

# Training existing model:
ketos train *.PNG --load baybayin_model_word_v5.mlmodel_96.mlmodel --output baybayin_model_word_v6.mlmodel --resize union --epochs 100 --quit fixed --min-epochs 100 --device cuda:0

# Training existing model that was trained on L mode images:
ketos train *.png --load pre-trained.mlmodel --output baybayin_model.mlmodel --resize union --epochs 30 --logger tensorboard --force-binarization

# Testing the model:
kraken -i <test-image> <output-text> segment ocr -m  <model-name.mlmodel>
kraken -i test_binarized.png test.txt segment ocr -m baybayin_model_v4.mlmodel_82.mlmodel --no-segmentation
kraken -i test_binarized.png test.txt ocr -m baybayin_model_v4.mlmodel_82.mlmodel --no-segmentation <-- single line