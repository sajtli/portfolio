# 📝 Offline Text Summarizer with LLMs

A fully offline, local-first text summarization tool powered by open-source large language models (LLMs) like Mistral — no APIs, no cloud, no internet needed after setup.

## 🚀 Project Overview

This project demonstrates how to build a usable, fast, and entirely local text summarization pipeline using quantized LLMs via [Ollama](https://ollama.com/). It's designed as a data science portfolio project with a focus on:

- Local deployment & LLM performance
- Practical prompt engineering
- Multimodal input support (future)
- Evaluation and explainability (future)

---

## 🔧 How to Run It

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/offline-text-summarizer.git
cd offline-text-summarizer

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies

```bash
pip install -r requirements.txt

💡 Currently empty — will be updated in future versions

### 4. Install and setup Ollama

Download from https://ollama.com/download

Install the Mistral model:

```bash
ollama run mistral

### 5. Run summarizer

```bash
python summarizer.py sample_data/long_article.txt


## ✅ Features (Phase 1)

 Summarize plain text files via terminal

 Works completely offline after setup

 Uses local Mistral model via Ollama


## Roadmap

| Status | Feature                                              |
| ------ | ---------------------------------------------------- |
| ✅      | Terminal summarizer with local Mistral model         |
| 🟡     | Streamlit or Gradio-based GUI                        |
| 🟡     | PDF input support                                    |
| 🟡     | Web article scraping (offline-safe)                  |
| 🟡     | Bullet-point vs paragraph summaries                  |
| 🟡     | Evaluation with ROUGE & readability scores           |
| 🟡     | RAG (retrieval-augmented generation) for long texts  |
| ⬜      | Explainability (sentence importance, heatmaps)       |
| ⬜      | Dockerized API version                               |
| ⬜      | Hugging Face Space deployment (optional online demo) |
| ⬜      | Blog post walkthrough                                |


## Folder structure

offline-text-summarizer/
├── summarizer.py
├── requirements.txt
├── sample_data/
│   └── long_article.txt
├── models/
│   └── README.md
├── README.md
└── .gitignore


## 🧠 Notes
The model is run via subprocess calls to ollama run mistral for simplicity.

You can swap in other Ollama-supported models like llama3, gemma, or codellama.

Later versions will use llama-cpp-python directly for full control and speed.


## 👤 Author
Built by Tamas David Horvath — Mechatronical Engineer, Data Scientist & LLM Enthusiast
