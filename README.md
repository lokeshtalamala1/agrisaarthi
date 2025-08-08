# AgriSaarthi: Multilingual AI Assistant for Farmers

AgriSaarthi is a voice-driven, multilingual AI assistant designed to help farmers in rural India get personalized agricultural guidance—even in offline settings. The system uses Retrieval-Augmented Generation (RAG), Whisper ASR, and multilingual speech synthesis.

## 🚀 Features
- 🎙 Voice input (via Gradio + Whisper)
- 🧠 RAG-based intelligent Q&A
- 🌐 Multilingual support (English, Hindi, Telugu, Tamil)
- 📡 Offline-friendly
- 🔊 Text-to-speech output using gTTS

## 📂 Project Structure

```
AgriSaarthi/
├── app.py                 # Gradio interface
├── config.py              # Language & system config
├── model_utils.py         # Model-based QA logic
├── rag_pipeline.py        # RAG workflow
├── voice_interface.py     # Transcription & speech synthesis
├── data/
│   ├── kb_facts.json      # Knowledge base
│   └── sample_queries.txt
├── demo/
│   ├── screenshot1.png
│   └── screenshot2.png
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## 🛠 Built With
- [Gradio](https://gradio.app/)
- [Whisper](https://github.com/openai/whisper)
- [gTTS](https://pypi.org/project/gTTS/)
- [Transformers](https://huggingface.co/transformers/)
- [FAISS](https://github.com/facebookresearch/faiss)

## 🧪 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

3. Talk to AgriSaarthi via microphone and get audio responses!

## 📋 Sample Query
> "When should I sow groundnut in the Kharif season?"

> "Groundnut should be sown in early June for the best yield in Kharif season."

## 📜 License
This project is for educational and hackathon use only.
