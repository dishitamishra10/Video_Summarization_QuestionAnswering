# 🎥 Video AI Assistant (Summarization + YouTube Q&A)

This project is an **AI-powered video assistant** that provides:

- 📺 YouTube Video Question Answering  
- 🎬 Video File Summarization  

It combines **LangChain, FastAPI, Streamlit, Whisper, OCR, and FAISS** to build a real-world multimedia AI system.

---

## 📂 Folder Structure

```bash
├── utils/
│   ├── Video_Summarizer/
│   │   ├── model.py          # Main summarization pipeline
│   │   ├── prompt.py         # Prompt template
│   │   ├── task_1.py         # Frame text extraction (OCR)
│   │   ├── task_2.py         # Audio transcription (Whisper)
│   │   ├── delete_all.py     # Cleanup temporary files
│   │
│   ├── Youtube_QNA/
│       ├── chain.py          # RAG pipeline
│       ├── vectorstore.py    # FAISS vector DB
│       ├── transcript.py     # Fetch YouTube transcript
│       ├── url_to_id.py      # Extract video ID
│
├── backend.py               # FastAPI backend
├── frontend.py              # Streamlit UI
├── requirements.txt         # Dependencies
├── .env                     # API keys (not to be shared)
```

---

## 🎯 Purpose

- Build a **multimodal AI system**
- Combine **video + audio + text understanding**
- Learn **RAG + Speech + OCR integration**
- Create real-world **AI-powered applications**

---

## 🧠 Core Concepts Used

- Retrieval-Augmented Generation (RAG)  
- FAISS Vector Database  
- Whisper (Speech-to-Text)  
- OCR using Tesseract  
- LangChain Chains  
- FastAPI Backend  
- Streamlit Frontend  

---

## ⚙️ How It Works

### 🔹 1. YouTube Q&A Flow

1. Extract video ID from URL  
2. Fetch transcript  
3. Convert to embeddings  
4. Store in FAISS  
5. Retrieve relevant chunks  
6. Generate answer using LLM  

📌 Implemented in:
- Backend API → :contentReference[oaicite:0]{index=0}  
- RAG Chain → :contentReference[oaicite:1]{index=1}  

---

### 🔹 2. Video Summarization Flow

1. Upload video file  
2. Extract frames → OCR text  
3. Extract audio → Whisper transcript  
4. Merge both texts  
5. Generate summary using LLM  

📌 Pipeline → :contentReference[oaicite:2]{index=2}  
📌 OCR → :contentReference[oaicite:3]{index=3}  
📌 Audio → :contentReference[oaicite:4]{index=4}  

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 2️⃣ Start Backend Server
```bash
uvicorn backend:app --reload
```

---

### 3️⃣ Run Frontend (Streamlit)
```bash
streamlit run frontend.py
```

---

## 💬 Features

- Ask questions about YouTube videos  
- Upload video and get AI summary  
- Dual-source summarization (audio + frames)  
- Context-aware answers using RAG  
- Clean interactive UI  

---

## 🧩 Architecture

```
User → Streamlit UI
     → FastAPI Backend
     → (YouTube OR Video Upload)

YouTube Flow:
→ Transcript → FAISS → LangChain → LLM → Answer

Video Flow:
→ Frames (OCR) + Audio (Whisper)
→ Merge → LLM → Summary
```

---

## ⚠️ Important Notes

- Requires FFmpeg installed (for frame extraction)  
- Requires Tesseract OCR installed  
- Whisper runs on CPU (may be slow)  
- Large videos take time to process  
- Do NOT upload `.env` file  

---

## 🚀 Future Improvements

- GPU acceleration for faster processing  
- Support multiple languages  
- Add video preview UI  
- Deploy as web application  
- Improve summarization accuracy  

---

## 👤 Author

**Dishita Mishra**  
CSE Student | AI & ML Enthusiast 🚀  

---

## ⭐ Final Note

This project demonstrates a **complete multimodal AI pipeline**, combining:

- Video processing  
- Speech recognition  
- OCR  
- Retrieval-based QA  

A strong real-world project for **AI + ML portfolio**.
