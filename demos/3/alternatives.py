from transformers import AutoModel

model = AutoModel.from_pretrained("google-bert/bert-base-cased", use_safetensors=True)
print(model)