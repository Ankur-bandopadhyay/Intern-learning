import os
import json
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def load_api_key():
    """Load the Gemini API key from .env, fail clearly if missing."""
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found. "
              "Did you create a .env file based on .env.example?")
        sys.exit(1)
    return api_key

def read_document(file_path):
    """Read a document from disk using a few common text encodings."""
    if not os.path.isfile(file_path):
        print(f"ERROR: file not found at {file_path}")
        sys.exit(1)

    with open(file_path, "rb") as f:
        raw_bytes = f.read()

    encodings = ["utf-8-sig", "utf-16", "utf-16-le", "utf-16-be", "cp1252", "latin-1"]
    for encoding in encodings:
        try:
            return raw_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue

    return raw_bytes.decode("utf-8", errors="replace")

def build_prompt(document_text):
    """This mirrors the template in day7-prompts/summarization-prompt.md"""
    return f"""You are a precise technical summarizer.
Read the document below and respond ONLY with valid JSON (no markdown fences, no extra text) in this exact schema:

{{
  "title": "short inferred title of the document",
  "summary": "3-4 sentence summary of the key content",
  "key_points": ["point 1", "point 2", "point 3"],
  "word_count": <integer, original document word count>
}}

Document:
\"\"\"
{document_text}
\"\"\"
"""

def call_gemini(prompt, api_key):
    """Call the Gemini API, with error handling for failed requests."""
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a concise assistant for engineers.",
                temperature=0,
                max_output_tokens=1024,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
            ),
        )
        return response.text
    except Exception as e:
        print(f"ERROR: API request failed: {e}")
        sys.exit(1)

def parse_and_print(raw_text):
    """Parse the model's JSON response and print individual fields."""
    cleaned = raw_text.strip()
    # Sometimes models wrap JSON in ```json fences even when told not to
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json\n", "", 1)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"ERROR: Could not parse model response as JSON: {e}")
        print("Raw response was:")
        print(raw_text)
        sys.exit(1)

    print("Title:      ", data.get("title"))
    print("Summary:    ", data.get("summary"))
    print("Key Points: ")
    for point in data.get("key_points", []):
        print("  -", point)
    print("Word Count: ", data.get("word_count"))

def main():
    parser = argparse.ArgumentParser(description="Summarize a document using Gemini.")
    parser.add_argument("file_path", help="Path to the document to summarize")
    args = parser.parse_args()

    api_key = load_api_key()
    document_text = read_document(args.file_path)
    prompt = build_prompt(document_text)
    raw_response = call_gemini(prompt, api_key)
    parse_and_print(raw_response)


if __name__ == "__main__":
    main()            


