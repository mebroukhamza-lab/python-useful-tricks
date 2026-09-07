# Python Usefull Tricks

A growing collection of small, single-purpose Python scripts for everyday automation: video, audio, images, PDFs, spreadsheets, web scraping, security, and messaging.

Each script does exactly one thing, uses one main library, and prints a clear confirmation when it's done.

## Quick start

```bash
git clone https://github.com/<your-username>/python-usefull-tricks.git
cd python-usefull-tricks
pip install -r requirements.txt
python <script-name>.py
```

Some scripts only need one library from the list — check the comment at the top of each file before installing everything.

## Scripts

### Video & GIF

| Script | What it does | Requires |
|---|---|---|
| `video-to-gif.py` | Converts a video clip into a GIF | `moviepy` |
| `trim-video.py` | Cuts a video down to a specific time range | `moviepy` |
| `merge-videos.py` | Concatenates two or more video files | `moviepy` |
| `extract-frames.py` | Extracts every frame of a video as an image | `opencv-python` |
| `compress-video.py` | Compresses a video by lowering its bitrate | `moviepy` |
| `extract-audio-from-video.py` | Extracts the audio track from a video file | `moviepy` |
| `video-to-mp3-batch.py` | Converts every video in a folder to MP3 | `moviepy` |
| `youtube-video-downloader.py` | Downloads a YouTube video in the best quality | `yt-dlp` |

### Audio & speech

| Script | What it does | Requires |
|---|---|---|
| `video-to-text-transcription.py` | Transcribes speech from a video using Whisper | `openai-whisper` |
| `text-to-speech.py` | Converts text into a spoken audio file | `gTTS` |
| `speech-to-text-mic.py` | Transcribes speech captured from the microphone | `SpeechRecognition pyaudio` |

### Images

| Script | What it does | Requires |
|---|---|---|
| `compress-image.py` | Compresses an image while keeping acceptable quality | `pillow` |
| `image-to-sketch.py` | Turns a photo into a pencil-sketch effect | `opencv-python` |
| `image-metadata-reader.py` | Reads EXIF metadata from a photo | `pillow` |
| `remove-image-background.py` | Removes the background from an image | `rembg pillow` |
| `face-detection.py` | Detects faces in an image and draws boxes around them | `opencv-python` |
| `webcam-capture.py` | Takes a photo using your webcam | `opencv-python` |
| `qr-code-scanner.py` | Reads and decodes a QR code from an image | `opencv-python` |
| `text-to-qrcode.py` | Turns any text or URL into a QR code image | `qrcode[pil]` |
| `barcode-generator.py` | Generates a barcode image from a code | `python-barcode` |
| `ocr-image-to-text.py` | Extracts text from an image using OCR | `pytesseract pillow` |

### PDF & documents

| Script | What it does | Requires |
|---|---|---|
| `images-to-pdf.py` | Combines several images into a single PDF | `pillow` |
| `merge-pdfs.py` | Merges several PDF files into one | `PyPDF2` |
| `pdf-to-text.py` | Extracts text from a PDF file | `PyPDF2` |
| `pdf-to-images.py` | Converts each page of a PDF into an image | `pdf2image` |
| `pdf-watermark.py` | Adds a watermark to every page of a PDF | `PyPDF2` |
| `pdf-password-protect.py` | Adds a password to protect a PDF file | `PyPDF2` |
| `word-to-pdf.py` | Converts a Word document into a PDF | `docx2pdf` |
| `read-write-docx.py` | Creates a Word document with a heading and paragraph | `python-docx` |

### Spreadsheets & data

| Script | What it does | Requires |
|---|---|---|
| `excel-to-csv.py` | Converts an Excel file to CSV | `openpyxl pandas` |
| `merge-excel-files.py` | Merges multiple Excel files into one | `pandas openpyxl` |
| `json-to-excel.py` | Converts a JSON file into an Excel spreadsheet | `pandas openpyxl` |
| `fake-data-generator.py` | Generates fake names and emails for testing | `faker` |

### Web & scraping

| Script | What it does | Requires |
|---|---|---|
| `check-website-status.py` | Checks whether a list of websites is up or down | `requests` |
| `download-all-images-from-page.py` | Downloads every image found on a web page | `requests beautifulsoup4` |
| `web-scraper-titles.py` | Scrapes and prints article titles from a page | `requests beautifulsoup4` |
| `website-screenshot.py` | Takes a full screenshot of a webpage | `selenium webdriver-manager` |
| `url-shortener.py` | Shortens a long URL | `pyshorteners` |
| `weather-checker.py` | Prints the current weather for a city | `requests` |
| `currency-converter.py` | Converts an amount between two currencies using live rates | `requests` |
| `track-ip-location.py` | Looks up geolocation info for an IP address | `requests` |
| `random-quote-generator.py` | Fetches a random inspirational quote | `requests` |

### Text & language

| Script | What it does | Requires |
|---|---|---|
| `translate-text.py` | Translates text into another language | `deep-translator` |
| `text-summarizer.py` | Summarizes a long text into key sentences | `sumy` |
| `detect-language.py` | Detects the language of a given text | `langdetect` |
| `spell-checker.py` | Finds and corrects misspelled words in a text | `pyspellchecker` |
| `sentiment-analysis.py` | Analyzes the sentiment polarity of a text | `textblob` |
| `text-to-morse.py` | Converts text into Morse code | `pymorse (or use built-in dict, no install needed)` |

### Downloaders

| Script | What it does | Requires |
|---|---|---|
| `instagram-image-download.py` | Downloads a public Instagram post | `instaloader` |
| `spotify-track-download.py` | Downloads a track from a Spotify link | `spotdl` |

### Security & files

| Script | What it does | Requires |
|---|---|---|
| `file-encryption.py` | Encrypts a file using a generated key | `cryptography` |
| `password-generator.py` | Generates a strong random password | `secrets (built-in, no install needed)` |
| `duplicate-file-finder.py` | Finds duplicate files in a folder by content hash | `os hashlib (built-in, no install needed)` |
| `batch-rename-files.py` | Renames every file in a folder with a consistent pattern | `os (built-in, no install needed)` |
| `pdf-password-protect.py` | Adds a password to protect a PDF file | `PyPDF2` |
| `wifi-password-viewer.py` | Lists saved Wi-Fi networks and their passwords (Windows) | `subprocess (built-in, no install needed) - Windows only` |

### Automation & messaging

| Script | What it does | Requires |
|---|---|---|
| `auto-mouse-mover.py` | Keeps your system awake by moving the mouse periodically | `pyautogui` |
| `auto-screenshot-timer.py` | Takes a screenshot every fixed interval | `pyautogui` |
| `clipboard-monitor.py` | Watches the clipboard and prints changes in real time | `pyperclip` |
| `send-email.py` | Sends an email through Gmail's SMTP server | `secure-smtplib (built-in smtplib, no install needed)` |
| `send-whatsapp-message.py` | Sends a WhatsApp message instantly | `pywhatkit` |
| `telegram-bot-message.py` | Sends a message through a Telegram bot | `python-telegram-bot` |
| `system-info.py` | Shows current CPU, RAM, and disk usage | `psutil` |

## Notes

- `wifi-password-viewer.py` only works on Windows (uses `netsh`).
- `send-whatsapp-message.py` and `telegram-bot-message.py` require your own phone number / bot token.
- `send-email.py` requires a Gmail app password, not your regular password.
- `video-to-text-transcription.py` (Whisper) and `remove-image-background.py` (rembg) download a model on first run.
- Scripts that open a webcam, microphone, or browser (Selenium) need the relevant hardware/driver available locally.

## License

MIT — see [LICENSE](LICENSE).
