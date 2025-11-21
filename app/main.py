from fastapi import FastAPI
from pydantic import BaseModel
from app.repo_sync import ensure_repo_exists, pull_repo, get_changed_files
from app.embeddings import process_file

from app.db import init_pgvector

@app.on_event("startup")
def startup_event():
    init_pgvector()


app = FastAPI(title="Impact Analyzer Listener")


class RepoUpdateEvent(BaseModel):
    repo: str               # org/name
    clone_url: str
    old_commit: str
    new_commit: str


@app.post("/repo-updated")
def repo_updated(event: RepoUpdateEvent):
    repo_name = event.repo.split("/")[-1]

    # 1. Ensure repo exists locally
    ensure_repo_exists(repo_name, event.clone_url)

    # 2. Pull latest changes
    pull_repo(repo_name)

    # 3. Identify changed files
    changed = get_changed_files(repo_name, event.old_commit, event.new_commit)

    # 4. Re-index changed files
    for file in changed:
        process_file(repo_name, file, event.new_commit)

    return {
        "status": "ok",
        "repo": repo_name,
        "changed_files": changed
    }
