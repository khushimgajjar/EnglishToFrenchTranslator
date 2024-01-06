# Text Translator Web App

This Flask web application utilizes the Googletrans library to provide real-time translation services. Users can input English text through the web interface, and the application will translate it to French. The translated text is then displayed on the screen.

## Setup

Make sure you have the required libraries installed:

```bash
pip install Flask googletrans==4.0.0-rc1
```

## How to Use

1. Run the Flask application using the provided script.
2. Access the application in your web browser (default: http://127.0.0.1:5000/).
3. Enter English text in the input field on the homepage.
4. Click the "Translate" button to see the corresponding French translation.

## Routes

- **Home ("/")**: Displays the homepage with an input field for English text.
- **Translate ("/translate")**: Handles the translation process and displays the original and translated text.

Feel free to customize the application by extending language support or incorporating additional features.
