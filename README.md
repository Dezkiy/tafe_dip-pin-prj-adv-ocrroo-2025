# Overview

This is a video player application that allows users to play and control videos using keyboard shortcuts. It also provides a way to view text that appears in video frames, helping users access information shown in the video more easily.

# Dependencies

- You will need the Python Imaging Library (PIL) (or the Pillow fork). Please check the Pillow documentation to know the basic Pillow installation.

- Install [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (additional info how to install the engine on Linux, Mac OSX and Windows). You must be able to invoke the tesseract command as tesseract. If this isn't the case, for example because tesseract isn't in your PATH, you will have to change the "tesseract_cmd" variable pytesseract.pytesseract.tesseract_cmd. Under Debian/Ubuntu you can use the package tesseract-ocr. For Mac OS users. please install homebrew package tesseract.

- pytesseract is a Python wrapper for Google's Tesseract-OCR Engine. It is available on PyPI and can be installed using pip:

# How to Run

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) engine (required for text extraction)
2. Place video files in the `resources/` folder
3. Install dependencies and start the server:

```sh
uv sync
uv run fastapi dev preliminary/simple_api.py
```

4. Open `http://127.0.0.1:8000` in a browser
