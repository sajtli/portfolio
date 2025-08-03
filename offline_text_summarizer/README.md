# Offline Text Summarizer with LLMs

A fully offline, local-first text summarization tool powered by open-source large language models (LLMs) like Mistral — no APIs, no cloud, no internet needed after setup.

## Project Overview

This project demonstrates how to build a usable, fast, and entirely local text summarization pipeline using quantized LLMs via [Ollama](https://ollama.com/). It's designed as a data science portfolio project with a focus on:

- Local deployment & LLM performance
- Prompt design for summarization styles
- CLI tools and argument parsing
- GUI, evaluation, and explainability (planned)

---

## How to Run It

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/offline-text-summarizer.git
cd offline-text-summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Currently empty — will be updated in future versions

### 4. Install and set up Ollama

- Download from: [https://ollama.com/download](https://ollama.com/download)

Install the Mistral model:

```bash
ollama run mistral
```

### 5. Run the summarizer

```bash
python summarizer.py sample_data/long_article.txt
```

---

## Features (Phase 1)

- [x] Summarize plain text files via terminal
- [x] Works completely offline after setup
- [x] Uses local Mistral model via Ollama
- [x] Supports multiple summary styles
- [x] Optional word-length input limiting
- [x] Custom prompt input
- [x] Colorized CLI output

---

## 🛠 CLI Options

```bash
python summarizer.py <input_file.txt> [--style STYLE] [--max-words N] [--custom-prompt PROMPT]
```

### Examples

```bash
# Default style
python summarizer.py sample_data/long_article.txt

# Bullet-point summary
python summarizer.py sample_data/long_article.txt --style bullet

# Limit input to 200 words
python summarizer.py sample_data/long_article.txt --max-words 200

# Custom prompt example
python summarizer.py sample_data/long_article.txt --custom-prompt "Summarize this like a Shakespearean sonnet"

# List all available styles
python summarizer.py list
```

---

## Available Styles

You can choose from the following summary styles:

| Style Name      | Description                        |
|------------------|------------------------------------|
| `default`        | Basic summary                      |
| `bullet`         | Bullet-point list                  |
| `simple`         | Child-friendly explanation         |
| `tweet`          | Tweet-length (280 characters)      |
| `executive`      | 3-sentence summary                 |
| `markdown`       | Markdown-formatted summary         |
| `headline`       | Three catchy headlines             |
| `meeting_notes`  | Structured notes with action items |
| `poetic`         | Short poem                         |
| `legal`          | Legal-style summary                |
| `snarky`         | Sarcastic tone                     |
| `listicle`       | Top 5 blog-style list              |
| `haiku`          | 3-line haiku                       |
| `steps`          | Step-by-step guide                 |

---

## Sample Output Examples

#### 🔹 Style: `bullet`

```text
🔸 The rise of AI is transforming industries  
🔸 Healthcare uses AI for diagnosis and precision surgery  
🔸 Finance leverages AI for fraud detection and trading  
🔸 Concerns include ethics, privacy, and job loss  
🔸 Experts urge responsible regulation
```

#### 🔹 Style: `tweet`

```text
AI is reshaping everything—from medicine to money—faster than ever. Great power, great responsibility. Stay curious, stay cautious. #AI
```

#### 🔹 Style: `simple`

```text
AI is like a super-smart robot helping people in hospitals, banks, and schools. But we need to be careful, so it doesn't cause problems like job loss or unfair treatment.
```

---

## Roadmap

| Status | Feature                                              |
|--------|------------------------------------------------------|
| ✅     | Terminal summarizer with local Mistral model         |
| ✅     | Summary style selector                               |
| ✅     | Word limit + prompt truncation                       |
| ✅     | Custom prompt support                                |
| 🟡     | Streamlit or Gradio-based GUI                        |
| 🟡     | PDF input support                                    |
| 🟡     | Web article scraping (offline-safe)                  |
| 🟡     | Bullet-point vs paragraph summaries                  |
| 🟡     | Evaluation with ROUGE & readability scores           |
| 🟡     | RAG (retrieval-augmented generation) for long texts  |
| ⬜     | Explainability (sentence importance, heatmaps)       |
| ⬜     | Dockerized API version                               |
| ⬜     | Hugging Face Space deployment (optional online demo) |
| ⬜     | Blog post walkthrough                                |

---

## Folder Structure

```
offline-text-summarizer/
├── summarizer.py
├── requirements.txt
├── sample_data/
│   └── long_article.txt
├── models/
│   └── README.md
├── README.md
└── .gitignore
```

---

## Notes

- The model is run via subprocess calls to `ollama run mistral` for simplicity.
- You can swap in other Ollama-supported models like `llama3`, `gemma`, or `codellama`.
- Later versions will use `llama-cpp-python` directly for full control and speed.

---

## Author

Built by Tamas David Horvath — Mechatronical Engineer, Data Scientist & LLM Enthusiast  
📫 [LinkedIn/GitHub link here]

---

## License

MIT License
