from app.db import get_db

def save_chunk(repo, file_path, chunk_index, content, embedding, commit_hash):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO code_chunks
        (repo_name, file_path, chunk_index, content, embedding, commit_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (repo_name, file_path, chunk_index)
        DO UPDATE SET
            content = EXCLUDED.content,
            embedding = EXCLUDED.embedding,
            commit_hash = EXCLUDED.commit_hash,
            updated_at = NOW();
    """, (repo, file_path, chunk_index, content, embedding, commit_hash))

    conn.commit()
    cur.close()
    conn.close()
