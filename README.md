# J.A.R.V.I.S - Your Personal Voice AI Assistant

## 📌 Project Overview
J.A.R.V.I.S is a Python-based voice assistant that can execute commands, browse the web, fetch news, play music, and even respond intelligently using OpenAI's API. This assistant listens for the wake word **"Jarvis"** and responds to voice commands accordingly.

## 🚀 Features
- ✅ **Web Browsing** – Open Google, Facebook, YouTube, and LinkedIn with voice commands.
- ✅ **News Updates** – Fetches real-time news using the NewsAPI.
- ✅ **Music Playback** – Plays songs from a predefined music library.
- ✅ **AI-Powered Responses** – Uses OpenAI's API for smart conversational replies.
- ✅ **Speech Recognition & Text-to-Speech** – Converts speech to text and responds using voice.

## 🏗️ Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - `speech_recognition` – For voice command recognition.
  - `webbrowser` – For opening websites.
  - `pyttsx3` / `gTTS` – For text-to-speech conversion.
  - `pygame` – For audio playback.
  - `requests` – For fetching news data.
  - `openai` – For AI-generated responses.

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-github-username/JARVIS-AI-Virtual-Assistant.git
   cd JARVIS-AI-Virtual-Assistant
   ```

2. **Install Dependencies**
   ```sh
   pip install speechrecognition pyttsx3 webbrowser requests pygame gtts openai
   ```

3. **Set Up API Keys**
   - Get an API key from **NewsAPI** (`https://newsapi.org`) and replace `newsapi="your news api"` in the script.
   - Get an API key from **OpenAI** (`https://platform.openai.com/`) and replace `api_key="your openAI api"` in the script.

4. **Run the Program**
   ```sh
   python main.py
   ```

## 🖥️ Usage Guide
- **Wake Word:** Say **"Jarvis"** to activate.
- **Commands:**
  - "Open Google" → Opens Google.
  - "Open Youtube" → Opens YouTube.
  - "Open LinkedIn" → Opens LinkedIn.
  - "News" → Fetches the latest headlines.
  - "Play [song_name]" → Plays the specified song.
  - Any other question → Gets a response from OpenAI.

## 💡 Future Enhancements
- Add more voice commands for productivity tasks.
- Improve speech recognition accuracy.
- Integrate with smart home devices.

## 🤝 Contribution
Feel free to contribute by:
- Reporting bugs 🐞
- Suggesting new features ✨
- Improving documentation 📖

## 📞 Contact
For any queries, reach out to me via:
- 📧 Email: pvashisth0711@gmail.com
- 🔗 GitHub: [pvashisth-07](https://github.com/pvashisth-07)
- 🔗 LinkedIn: [Pranav Vashisth](https://www.linkedin.com/in/pranav-vashisth/)

---
_Enjoy hands-free assistance with J.A.R.V.I.S! 🎙️_
