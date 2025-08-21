from kraken.lib.models import load_any
model = load_any('baybayin_model_word_v1.mlmodel_99.mlmodel')
print(sorted(model.codec.c2l.keys()))
