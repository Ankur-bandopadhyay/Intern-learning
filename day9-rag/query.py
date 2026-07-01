import os
import sys
import json
import numpy as np
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

# LOAD THE SAVED EMBEDDINGS
def load_embeddings(path="embeddings.json"):
    """Load previously saved chunks + embeddings."""
    if not os.path.isfile(path):
        print(f"ERROR: {path} not found. Run ingest.py first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
#GET EMBEDDINGS FOR THE QUESTION
def get_embedding(client, text):
    """Get an embedding vector for a piece of text."""
    try:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )
        return response.embeddings[0].values
    except Exception as e:
        print(f"ERROR: Failed to get embedding: {e}")
        sys.exit(1)

#COSINE SIMILARITY
def cosine_similarity(a, b):
    """Return a similarity score between -1 and 1 for two vectors."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

#FIND AND PRINT top-3 MATCHES
def top_matches(question_embedding, data, top_n=3):
    """Return the top N chunks most similar to the question."""
    scored = []
    for item in data:
        score = cosine_similarity(question_embedding, item["embedding"])
        scored.append((score, item["text"]))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_n]


def print_results(question, results):
    print(f"\nQuestion: {question}\n")
    for rank, (score, text) in enumerate(results, start=1):
        print(f"#{rank}  score={score:.4f}")
        print(f"{text}\n")

#main()
def main():
    api_key = load_api_key()
    client = genai.Client(api_key=api_key)
    data = load_embeddings()

    question = input("Enter your question: ")
    question_embedding = get_embedding(client, question)

    results = top_matches(question_embedding, data, top_n=3)
    print_results(question, results)


if __name__ == "__main__":
    main()

    


