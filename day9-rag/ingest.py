import os
import sys
import json
from dotenv import load_dotenv
from google import genai

def load_api_key():

    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("ERROR: GEMINI_API_KEY not found. "
              "Did you create a .env file based on .env.example?")
        sys.exit(1)
    return api_key

def read_document(file_path):
    """Read the source document from disk."""
    if not os.path.isfile(file_path):
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
#CHUNKING FUNCTION (WITH ADJUSTIBLE SIZE AND OVERLAP)
def chunk_text(text, size=150, overlap=50):
    """Split text into overlapping chunks of `size` characters."""
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        chunks.append(chunk.strip())
        start += size - overlap
    # Remove any empty chunks caused by trailing whitespace
    return [c for c in chunks if c]   

#GET AN EMBEDDING FOR ONE PIECE OF TEXT
def get_embedding(client, text, task_type="retrieval_document"):
    """Get an embedding vector for a piece of text using Gemini's embedding model."""
    try:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )
        return response.embeddings[0].values
    except Exception as e:
        print(f"ERROR: Failed to get embedding: {e}")
        sys.exit(1)

def embed_chunks(client, chunks):
    """Generate embeddings for every chunk."""
    data = []
    print(f"Embedding {len(chunks)} chunks...")
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(client, chunk)
        data.append({"chunk_id": i, "text": chunk, "embedding": embedding})
        print(f"  Chunk {i+1}/{len(chunks)} embedded")
    return data


def save_embeddings(data, output_path="embeddings.json"):
    """Save chunks + embeddings to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} chunks to {output_path}")

def main():
    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    document_text = read_document("source_document.txt")

    # Adjustable parameters — change these to test different chunking strategies
    chunk_size = 150
    chunk_overlap = 50

    chunks = chunk_text(document_text, size=chunk_size, overlap=chunk_overlap)
    print(f"Document split into {len(chunks)} chunks (size={chunk_size}, overlap={chunk_overlap})")

    data = embed_chunks(client, chunks)
    save_embeddings(data)


if __name__ == "__main__":
    main()            