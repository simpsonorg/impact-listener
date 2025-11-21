from openai import OpenAI
from app.models import save_chunk
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_text(text, size=800):
    return [text[i:i+size] for i in range(0, len(text), size)]

def embed_content(text):
    res = client.embeddings.create(
        model="text-embedding-3-large",
        input=[text]
    )
    return res.data[0].embedding

def process_file(repo, file_path, commit_hash):
    abs_path = f"/data/repos/{repo}/{file_path}"

    if not os.path.exists(abs_path):
        return

    with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
        src = f.read()

    chunks = chunk_text(src)

    for idx, chunk in enumerate(chunks):
        vector = embed_content(chunk)
        save_chunk(repo, file_path, idx, chunk, vector, commit_hash)
