# Offline Text Summarizer with LLMs

Run local, GPU-accelerated text summarization using open-source large language models — no internet, no APIs, no tokens required.

Built as a real-world project for my data science portfolio, this CLI tool summarizes any `.txt` file using [Mistral 7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1), powered by `llama-cpp-python`.

---

## Features (Phase 2)

- Works 100% offline with quantized `.gguf` models
- Powered by [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) + CUDA (GPU acceleration)
- Choose from 12+ summary styles (executive, tweet, bullet, legal, poetic, etc.)
- Option to use your own custom prompt
- Control the max output length via `--max-tokens`
- Colorized terminal output with `colorama`

---

## Installation

1. Install Python 3.11  
2. Install [CUDA Toolkit 12.4](https://developer.nvidia.com/cuda-12-4-0-download-archive)  
3. Clone this repo:
   ```bash
   git clone https://github.com/tdhorvathds/offline_text_summarizer.git
   cd offline_text_summarizer
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Model Setup

Download the [Mistral-7B-Instruct-v0.1 Q4_K_M .gguf model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) and place it here:

```
C:/Users/yourusername/llama/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

---

## How to Use

### List available summary styles:

```bash
python summarizer.py list
```

### Run with a predefined style:

```bash
python summarizer.py sample_data/article.txt --style executive
```

### Use a custom prompt:

```bash
python summarizer.py sample_data/report.txt --custom-prompt "Summarize for a LinkedIn post"
```

### Limit output length:

```bash
python summarizer.py sample_data/paper.txt --style bullet --max-tokens 150
```

---

## Summary Styles Available

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

## Why This Project?

This project is part of my personal data science portfolio. I wanted to:

- Learn how to work directly with local LLMs and quantized models
- Explore performance with CUDA + `llama-cpp`
- Build a practical NLP tool with real command-line usability
- Document my workflow for future experiments and employers

---

## Roadmap

| Status | Feature                                                      |
|--------|--------------------------------------------------------------|
| ✅     | Terminal summarizer with local Mistral model         |
| ✅     | Summary style selector                               |
| ✅     | Word limit + prompt truncation                       |
| ✅     | Custom prompt support                                |
| ✅     | GPU-accelerated summarization using llama-cpp & Mistral 7B  |
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

## Credits

- [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [TheBloke GGUF Models](https://huggingface.co/TheBloke)

---

## Author

Built by [Tamas David Horvath](https://github.com/tdhorvathds)  
Let's connect on [LinkedIn](https://www.linkedin.com/in/tdhorvathds/)
