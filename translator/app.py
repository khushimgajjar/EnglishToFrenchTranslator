from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form.get('text')

    if not input_text:
        return "Text not provided"

    translator = Translator()
    translated = translator.translate(input_text, src='en', dest='fr')
    translated_text = translated.text

    return f"English text: {input_text}<br>French text: {translated_text}"

if __name__ == '__main__':
    app.run(debug=True)
