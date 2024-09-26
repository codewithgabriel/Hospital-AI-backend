from transformers import MarianMTModel, MarianTokenizer

model_name = "gabri3l/hospital-ai-nupe-to-yor"
print(f'Loading Nupe to Yoruba model from {model_name}')
tokenizer_nupe_to_yor = MarianTokenizer.from_pretrained(model_name)
model_nupe_to_yor = MarianMTModel.from_pretrained(model_name)
print(f'Model loaded successfully')
print("*" * 50)
