import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    return psycopg2.connect(
        os.getenv("DATABASE_URL"),
        sslmode="require",
        cursor_factory=RealDictCursor
    )

def init_pgvector():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS code_chunks (
            id SERIAL PRIMARY KEY,
            repo_name TEXT,
            file_path TEXT,
            chunk_index INT,
            content TEXT,
            embedding vector(1536),
            commit_hash TEXT,
            updated_at TIMESTAMP DEFAULT NOW(),
            UNIQUE(repo_name, file_path, chunk_index)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
