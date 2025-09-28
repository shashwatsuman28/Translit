# app.py
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import io
import pytesseract
from pytesseract import Output

# Optional: python transliteration library
try:
    from indic_transliteration.sanscript import transliterate as py_transliterate
    from indic_transliteration.sanscript import SCHEMES
except Exception:
    py_transliterate = None

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/transliterate', methods=['POST'])
def transliterate_api():
    """
    Accepts multipart/form-data 'image' and form fields:
      - from_script (e.g. 'devanagari', 'tamil', 'gurmukhi')
      - to_script (e.g. 'itrans', 'devanagari', etc.)
    Returns bounding boxes and transliterated text.
    """
    file = request.files.get('image')
    from_script = request.form.get('from_script', 'devanagari')
    to_script = request.form.get('to_script', 'devanagari')

    if not file:
        return jsonify({'error': 'no image'}), 400

    img = Image.open(io.BytesIO(file.read()))
    # Use pytesseract to get boxes and text
    data = pytesseract.image_to_data(img, lang='eng+hin+tam+pan+kan+tel+mal', output_type=Output.DICT)

    results = []
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        text = data['text'][i].strip()
        if not text:
            continue
        left = int(data['left'][i])
        top = int(data['top'][i])
        width = int(data['width'][i])
        height = int(data['height'][i])

        # Do transliteration (if python lib present)
        if py_transliterate:
            try:
                ttext = py_transliterate(text, from_script, to_script)
            except Exception:
                ttext = text
        else:
            # fallback: return same text so frontend can transliterate with JS
            ttext = text

        results.append({
            'text': text,
            'transliteration': ttext,
            'bbox': [left, top, width, height]
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
