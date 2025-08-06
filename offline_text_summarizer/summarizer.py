import argparse
from pathlib import Path
from colorama import Fore, Style, init
from llama_cpp import Llama

# Initialize colorama
init()

# Load Mistral only once
llm = Llama(
    model_path="D:/github/portfolio/offline_text_summarizer/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_gpu_layers=-1,
    n_ctx=4096,
    verbose=False
)

# Predefined summary styles
style_prompts = {
    "default": "Summarize the following text.",
    "bullet": "Summarize the following in bullet points.",
    "simple": "Summarize like you're explaining it to a 10-year-old.",
    "tweet": "Summarize in under 280 characters.",
    "executive": "Give a concise 3-sentence executive summary.",
    "markdown": "Summarize with Markdown headings and bullet points.",
    "headline": "Give 3 catchy news-style headlines.",
    "meeting_notes": "Convert into structured meeting notes with action items.",
    "poetic": "Summarize the following as a short poem.",
    "snarky": "Summarize this with sarcasm and wit.",
    "steps": "Convert this into a step-by-step guide."
}



def smart_truncate(text, max_words=150):
    import re
    words = text.split()
    if len(words) <= max_words:
        return text

    truncated = " ".join(words[:max_words + 20])
    sentences = re.split(r'(?<=[.!?])\s+', truncated)

    clean = ""
    count = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if count + word_count > max_words:
            break
        clean += sentence.strip() + " "
        count += word_count

    return clean.strip()

def summarize(text, style="default", custom_prompt=None, max_tokens=200):
    if custom_prompt:
        prompt = f"{custom_prompt}\n\n{text}\n\nSummary:"
    else:
        prompt = f"{style_prompts.get(style, style_prompts['default'])}\n\n{text}\n\nSummary:"

    print(Fore.YELLOW + "\n⏳ Generating summary using Mistral..." + Style.RESET_ALL)

    response = llm(prompt, max_tokens=max_tokens, stop=["</s>"])
    return smart_truncate(response["choices"][0]["text"].strip(), max_words=max_tokens)

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def print_available_styles():
    print(Fore.BLUE + "\nAvailable Summary Styles:\n" + Style.RESET_ALL)
    for key in style_prompts.keys():
        print(f"  - {key}")
    print()

def main():
    parser = argparse.ArgumentParser(description="Offline GPU LLM Summarizer (Mistral)")
    parser.add_argument("input", nargs='?', help="Path to a .txt file or 'list' for styles")
    parser.add_argument("--style", default="default", choices=list(style_prompts.keys()), help="Summary style")
    parser.add_argument("--custom-prompt", type=str, help="Custom prompt to override summary style")
    parser.add_argument("--max-tokens", type=int, default=200, help="Max output tokens")

    args = parser.parse_args()

    if args.input == "list":
        print_available_styles()
        return

    if not args.input:
        print(Fore.RED + "Please provide a .txt file or use 'list'" + Style.RESET_ALL)
        return

    input_path = Path(args.input)
    if not input_path.exists():
        print(Fore.RED + f"File not found: {input_path}" + Style.RESET_ALL)
        return

    text = read_text_file(input_path)
    summary = summarize(text, style=args.style, custom_prompt=args.custom_prompt, max_tokens=args.max_tokens)

    print(Fore.GREEN + "\nSummary:\n" + Style.RESET_ALL)
    print(Fore.CYAN + summary + Style.RESET_ALL)

if __name__ == "__main__":
    main()
