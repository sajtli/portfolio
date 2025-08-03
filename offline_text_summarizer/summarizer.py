import subprocess
import argparse
from pathlib import Path

def summarize(text):
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode().strip()

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Offline LLM-based Text Summarizer")
    parser.add_argument("input", help="Path to a .txt file to summarize")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        return

    text = read_text_file(input_path)
    print("\n🔍 Summarizing...\n")
    summary = summarize(text)
    print("\n📝 Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
