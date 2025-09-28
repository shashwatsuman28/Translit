<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- <title>ScriptTranslit - README
</title> -->
<!-- <style>
  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #111; color: #eee; margin: 0; padding: 0; }
  header { background: #222; padding: 20px; text-align: center; border-bottom: 3px solid #ffcc00; }
  header h1 { margin: 0; color: #ffcc00; }
  header p { color: #ccc; margin: 5px 0 0; font-size: 1.1em; }
  main { padding: 20px; max-width: 900px; margin: auto; }
  h2 { color: #ffcc00; border-bottom: 1px solid #444; padding-bottom: 6px; }
  ul { line-height: 1.6; }
  code { background: #222; color: #ffcc00; padding: 2px 6px; border-radius: 4px; }
  pre { background: #222; color: #ffcc00; padding: 12px; border-radius: 6px; overflow-x: auto; }
  .note { background: #333; padding: 10px 12px; border-left: 4px solid #ffcc00; margin: 10px 0; }
  footer { text-align: center; padding: 20px; border-top: 1px solid #444; color: #888; }
  a { color: #ffcc00; text-decoration: none; }
  a:hover { text-decoration: underline; }
</style> -->
</head>
<body>
<header>
  <h1>ScriptTranslit</h1>
  <p>Indian Script OCR & Transliteration PWA</p>
</header>

<main>
  <h2>✨ Features</h2>
  <ul>
    <li>📷 <strong>Camera Capture:</strong> Take a photo of any text with your device camera.</li>
    <li>🔄 <strong>Re-Capture:</strong> Retake images without reloading the app.</li>
    <li>✏️ <strong>Selection Tool:</strong> Select specific regions for OCR & transliteration.</li>
    <li>📝 <strong>Multi-Script OCR:</strong> Supports Hindi, Tamil, Punjabi, Telugu, Kannada, Malayalam & English.</li>
    <li>⚡ <strong>Automatic Script Detection:</strong> Detects script of each word automatically.</li>
    <li>🔤 <strong>Transliteration:</strong> Convert text between Indian scripts and Latin (IAST).</li>
    <li>🖼️ <strong>Gallery:</strong> Stores captured images & transliterations.</li>
    <li>📱 <strong>Touch & Mouse Support:</strong> Works on mobile & desktop.</li>
    <li>⏳ <strong>Loading Indicator:</strong> Shows progress while transliterating.</li>
  </ul>

  <h2>🗂 Supported Scripts</h2>
  <ul>
    <li>Devanagari (हिंदी)</li>
    <li>Gurmukhi (ਪੰਜਾਬੀ)</li>
    <li>Tamil (தமிழ்)</li>
    <li>Telugu (తెలుగు)</li>
    <li>Kannada (ಕನ್ನಡ)</li>
    <li>Malayalam (മലയാളം)</li>
    <li>Latin (IAST/English)</li>
  </ul>

  <h2>⚙️ Requirements</h2>
  <ul>
    <li>Modern web browser (Chrome, Firefox, Edge, Safari)</li>
    <li>Camera access on device</li>
    <li>No backend required; fully client-side</li>
    <li>Optional: Local server (e.g., VS Code Live Server) for mobile testing</li>
  </ul>

  <h2>🚀 Setup & Usage</h2>
  <ol>
    <li>Clone or download the repository.</li>
    <li>Open <code>index.html</code> in a modern browser.</li>
    <li>Allow camera access when prompted.</li>
    <li>Click <strong>Capture</strong> to take a photo of text.</li>
    <li>Drag to select the area you want to transliterate (touch or mouse).</li>
    <li>Choose the target script from the dropdown.</li>
    <li>Click <strong>Transliterate Selection</strong> to overlay transliterated text.</li>
    <li>Captured images & transliterations appear in the gallery.</li>
    <li>Use <strong>Re-Capture</strong> to take a new photo.</li>
  </ol>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li><a href="https://github.com/naptha/tesseract.js">Tesseract.js</a> – OCR engine for image text recognition.</li>
    <li><a href="https://github.com/indic-transliteration/sanscript.js">Sanscript.js</a> – Transliteration library for Indian scripts.</li>
    <li>HTML, CSS, JavaScript – Core web technologies.</li>
    <li>Progressive Web App (PWA) ready for mobile usage.</li>
  </ul>

  <h2>⚠️ Known Issues / Notes</h2>
  <div class="note">
    <ul>
      <li>Transliteration may fail if text is partially recognized incorrectly.</li>
      <li>OCR accuracy depends on lighting, font, and camera quality.</li>
      <li>Best experience on modern smartphones with rear camera.</li>
    </ul>
  </div>

  <h2>📜 License</h2>
  <p>MIT License. Free to use and modify.</p>

  <h2>🔮 Future Improvements</h2>
  <ul>
    <li>Support more Indian scripts like Oriya & Assamese.</li>
    <li>Batch OCR for multiple images.</li>
    <li>Export transliterated text to PDF or DOCX.</li>
    <li>Offline caching for PWA use without internet.</li>
    <li>Better UI for multi-line text selection and editing.</li>
  </ul>
</main>

<footer>
  Made with ❤️ by [Your Name] | ScriptTranslit PWA
</footer>
</body>
</html>
