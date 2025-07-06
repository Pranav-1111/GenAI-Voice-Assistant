# 🗣️ AI Voice Assistant – GenAI Project

An intelligent voice-enabled assistant built with open-source GenAI technologies. This assistant converts voice to text using OpenAI's Whisper, processes user queries through a locally hosted LLM (TinyLlama) using LangChain, and responds back using Text-to-Speech (TTS). It supports wake-word detection for seamless interaction and utilizes FAISS for persistent memory and contextual conversations.

## 🚀 Features

- 🎙️ **Voice to Text**: Converts spoken input into text using OpenAI's Whisper.
- 🧠 **Natural Language Understanding**: Leverages LangChain + TinyLlama (local LLM) for contextual query understanding and generation.
- 🗣️ **Text to Speech**: Responds using gTTS (Google Text-to-Speech).
- 💾 **Memory with FAISS**: Stores and retrieves previous interactions for contextual memory.
- 🔊 **Wake-Word Detection**: Enables always-on assistant functionality.
- 🌐 **Streamlit UI**: Clean, interactive web interface to communicate with the assistant.

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **TinyLlama (via Hugging Face Transformers)**
- **Whisper (OpenAI)**
- **gTTS**
- **FAISS**
- **Streamlit**
- **PyTorch**

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-voice-assistant-genai.git
cd ai-voice-assistant-genai
pip install -r requirements.txt
```

Make sure to have `ffmpeg` installed and added to your system path for audio handling.

## 🧪 Run the App

```bash
streamlit run main.py
```

Speak your query after the wake word is detected. The assistant will listen, process, and respond vocally.

## 🧠 Architecture

```plaintext
[🎤 Mic Input] → [🌀 Whisper STT] → [🧠 LangChain + TinyLlama] → [🗂 FAISS Memory]
                                                        ↓
                                                [🗣️ gTTS TTS Output]
                                                        ↓
                                               [🔊 Audio Response]
```

## 📁 Project Structure

```
.
├── main.py               # Streamlit app launcher
├── voice_input.py        # Handles microphone input and wake-word detection
├── whisper_stt.py        # Whisper integration for speech-to-text
├── llm_response.py       # LangChain + TinyLlama LLM logic
├── tts_output.py         # Text-to-speech response
├── memory_faiss.py       # FAISS-based vector memory store
├── requirements.txt
└── README.md
```

## 🧠 Future Enhancements

- Multilingual support
- Emotion-aware responses
- Integration with external APIs for weather, calendar, etc.

## 🤝 Contribution

Feel free to open issues or submit pull requests for enhancements or bug fixes.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Built with ❤️ using open-source AI.