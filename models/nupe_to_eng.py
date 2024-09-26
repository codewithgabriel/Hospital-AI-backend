from transformers import MarianMTModel, MarianTokenizer

model_name = "gabri3l/hospital-ai-nupe-to-eng"
print(f'Loading Nupe to English model from {model_name}')
tokenizer_nupe_to_eng = MarianTokenizer.from_pretrained(model_name)
model_nupe_to_eng = MarianMTModel.from_pretrained(model_name)
print(f'Model loaded successfully')
print("*" * 50)
