from transformers import MarianMTModel, MarianTokenizer

model_name = "gabri3l/hospital-ai-yor-to-eng"
print(f'Loading Yoruba to English model from {model_name}')
tokenizer_yor_to_eng = MarianTokenizer.from_pretrained(model_name)
model_yor_to_eng = MarianMTModel.from_pretrained(model_name)
print(f'Model loaded successfully')
print("*" * 50)
