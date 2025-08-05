import subprocess
import argparse
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama for Windows terminal compatibility
init()

# Predefined summary styles
style_prompts = {
    "default": "Summarize the following text.",
    "bullet": "Summarize the following in bullet points.",
    "simple": "Summarize this like you're explaining it to a 10-year-old.",
    "tweet": "Summarize the following in under 280 characters.",
    "executive": "Provide a concise 3-sentence executive summary.",
    "markdown": "Summarize this using Markdown formatting with headings and bullet points.",
    "headline": "Summarize the following using 3 catchy news headlines.",
    "meeting_notes": "Convert the text into structured meeting notes with action items.",
    "poetic": "Summarize the following as a short poem.",
    "legal": "Summarize the following like a legal case brief.",
    "snarky": "Summarize this with a sarcastic and witty tone.",
    "listicle": "Summarize the following as a top 5 list, like a blog article.",
    "haiku": "Summarize the text in a 3-line haiku format.",
    "steps": "Convert this text into a clear step-by-step guide."
}

def summarize(text, style="default", custom_prompt=None, max_words=None, max_output_words=None):
    # Input truncation
    if max_words:
        words = text.split()
        if len(words) > max_words:
            text = " ".join(words[:max_words])
            print(Fore.MAGENTA + f"\n⚠️ Input truncated to first {max_words} words.\n" + Style.RESET_ALL)

    # Build prompt
    if custom_prompt:
        prompt = f"{custom_prompt}\n\n{text}\n\nSummary:"
    else:
        if style not in style_prompts:
            print(Fore.RED + f"❌ Unsupported summary style: {style}" + Style.RESET_ALL)
            return None
        prompt = f"{style_prompts[style]}\n\n{text}\n\nSummary:"

    print(Fore.YELLOW + "\n⏳ Running local LLM via Ollama (mistral)...\n" + Style.RESET_ALL)
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )

    summary = result.stdout.decode().strip()

    # Output truncation
    if max_output_words:
        output_words = summary.split()
        if len(output_words) > max_output_words:
            summary = " ".join(output_words[:max_output_words])
            print(Fore.MAGENTA + f"\n⚠️ Output truncated to first {max_output_words} words.\n" + Style.RESET_ALL)

    return summary

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def print_available_styles():
    print(Fore.BLUE + "\n📚 Available Summary Styles:\n" + Style.RESET_ALL)
    for key in style_prompts.keys():
        print(f"  - {key}")
    print()

def main():
    parser = argparse.ArgumentParser(description="Offline LLM-based Text Summarizer")
    parser.add_argument("input", nargs='?', help="Path to a .txt file to summarize, or 'list' to view styles")
    parser.add_argument("--style", default="default", choices=list(style_prompts.keys()),
                        help="Choose a predefined summary style")
    parser.add_argument("--custom-prompt", type=str, help="Use a custom prompt instead of predefined styles")
    parser.add_argument("--max-words", type=int, help="Maximum number of input words to process")
    parser.add_argument("--max-output-words", type=int, help="Maximum number of words allowed in the output summary")

    args = parser.parse_args()

    if args.input == "list":
        print_available_styles()
        return

    if not args.input:
        print(Fore.RED + "❌ No input file provided. Please provide a path to a text file or use 'list'." + Style.RESET_ALL)
        return

    input_path = Path(args.input)
    if not input_path.exists():
        print(Fore.RED + f"❌ File not found: {input_path}" + Style.RESET_ALL)
        return

    text = read_text_file(input_path)
    summary = summarize(text, style=args.style, custom_prompt=args.custom_prompt, max_words=args.max_words, max_output_words=args.max_output_words)

    if summary:
        print(Fore.GREEN + "\n✅ Summary:\n" + Style.RESET_ALL)
        print(Fore.CYAN + summary + Style.RESET_ALL)

if __name__ == "__main__":
    main()
