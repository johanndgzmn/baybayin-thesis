# Setup
1. Create a virtual environment ``` python -m venv kraken ```
2. Activate virtual environment ``` Scripts\activate```
3. Install dependencies
```
pip install kraken
pip install tensorflow
```
# Dataset
Use the dataset (i) to train the model. Gradually train the model by starting from characters, to words, then sentences.

# Training existing model:
```ketos train *.jpg --load pre-trained.mlmodel --output baybayin_new_symbols.mlmodel --resize union --epochs 100 --quit early --min-epochs 10 --device cuda:0 --lrate 0.0005 2>&1 | tee training.log ```

Enter ```$env:PYTHONIOENCODING="utf-8"``` in the terminal before training.

# Testing the model:
General usage:
kraken -i test-image output-text segment ocr -m  model-name.mlmodel

```kraken -i test_binarized.png test.txt segment ocr -m baybayin_model_v4.mlmodel_82.mlmodel``` <-- entire page

```kraken -i test_binarized.png test.txt ocr -m baybayin_model_v4.mlmodel_82.mlmodel --no-segmentation``` <-- single line

# Testing
Use baybayin_custom_dataset_edited.mlmodel_best.mlmodel for testing.

# Credits
Word images - https://github.com/rbp0803/Baybayin-Word-Images
Character images - https://www.kaggle.com/datasets/jamesnogra/baybayn-baybayin-handwritten-images