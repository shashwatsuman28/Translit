ScriptTranslit - Indian Script OCR & Transliteration PWA

ScriptTranslit is a Progressive Web App (PWA) that allows users to capture text from images and transliterate it between multiple Indian scripts and Latin (IAST). The app uses Tesseract.js for OCR and Sanscript.js for transliteration.

Features

Camera Capture: Take a photo of any text using your device camera.

Re-Capture: Retake images without reloading the app.

Selection Tool: Select a specific region of the captured image for OCR and transliteration.

Multi-Script OCR: Recognizes text in Hindi, Tamil, Punjabi (Gurmukhi), Telugu, Kannada, Malayalam, and English.

Automatic Script Detection: Detects the script of each recognized word.

Transliteration: Convert text between Indian scripts and Latin (IAST).

Gallery: Stores captured images along with their transliterations.

Touch and Mouse Support: Works on mobile and desktop devices.

Loading Indicator: Shows a visual indicator when transliteration is in progress.

Supported Scripts

Devanagari (हिंदी)

Gurmukhi (ਪੰਜਾਬੀ)

Tamil (தமிழ்)

Telugu (తెలుగు)

Kannada (ಕನ್ನಡ)

Malayalam (മലയാളം)

Latin (IAST/English)

Requirements

Modern web browser (Chrome, Firefox, Edge, Safari)

Camera access on device

No backend required; fully client-side

Optional for development:

Local server (e.g., VS Code Live Server) for mobile testing

Setup & Usage

Clone or download the repository.

Open index.html in a modern browser.

Allow camera access when prompted.

Use the Capture button to take a photo of the text.

Select the area you want to transliterate by dragging on the screen (touch or mouse).

Choose the target script from the dropdown.

Click Transliterate Selection to view the transliteration overlay.

Captured images and transliterations appear in the gallery.

Use Re-Capture to take a new photo.

Technologies Used

Tesseract.js
 – OCR engine for recognizing text in images.

Sanscript.js
 – Transliteration library for Indian scripts.

HTML, CSS, JavaScript – Core web technologies.

Progressive Web App (PWA) ready for mobile usage.

Known Issues / Notes

Transliteration may fail if text is partially recognized incorrectly.

OCR accuracy depends on lighting, font, and camera quality.

Best experience on modern smartphones with rear camera.
