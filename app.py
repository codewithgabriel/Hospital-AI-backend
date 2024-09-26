from flask import Flask, request, jsonify
from flask_cors import CORS



# Initialize Flask app
app = Flask(__name__)
CORS(app)

# First load all the model
from models.yor_to_eng import tokenizer_yor_to_eng , model_yor_to_eng 
from models.nupe_to_eng import tokenizer_nupe_to_eng , model_nupe_to_eng
from models.nupe_yor import tokenizer_nupe_to_yor , model_nupe_to_yor

# Function to handle translation yoruba to english
def translate_text_yor_to_eng(sentence):
    tokenizer = tokenizer_yor_to_eng
    model = model_yor_to_eng
    
    input_text = sentence
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Function to handle translation nupe to english
def translate_text_nupe_to_eng(sentence):
    tokenizer = tokenizer_nupe_to_eng
    model = model_nupe_to_eng
    
    input_text = sentence
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Function to handle translation nupe to yoruba
def translate_text_nupe_to_yor(sentence):
    tokenizer = tokenizer_nupe_to_yor
    model = model_nupe_to_yor
    
    input_text = sentence
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Define a route for translation
@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Expecting JSON payload: {"src_lang": "en", "tgt_lang": "fr", "text": "Hello!"}
        data = request.json
        text = data.get('text', '')
        src_lang = data.get('src_lang' , 'en')  # Default to English
        tgt_lang = data.get('tgt_lang' , 'yo')  # Default to Yoruba
        
        print(text , src_lang , tgt_lang)
        translated_text = translate_text_yor_to_eng(text)

        if not text:
            return jsonify({"error": True, "message": "Text to translate is missing."}), 400

        # Perform translation
        lt_type = src_lang + "-" + tgt_lang
        if (lt_type == 'yo-en'):
            translated_text = translate_text_yor_to_eng(text)
            
        elif (lt_type ==  'nu-en'): 
            translated_text = translate_text_nupe_to_eng(text)
            
        elif (lt_type ==  'nu-yo'):
             translated_text = translate_text_nupe_to_yor(text)
        else:
            translate = 'Not Available'

        # Return the translated text as JSON
        return jsonify({"translated_text": translated_text, "error": False})
    
    except Exception as e:
        return jsonify({"error": True, "message": f"Translation failed: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8080 , host='0.0.0.0')
