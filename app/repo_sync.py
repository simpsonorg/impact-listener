import os
import subprocess
from git import Repo

BASE_REPO_DIR = "/data/repos"  # persistent storage

def ensure_repo_exists(repo_name, clone_url):
    repo_path = f"{BASE_REPO_DIR}/{repo_name}"

    # Clone if not exists
    if not os.path.exists(repo_path):
        print(f"Cloning {repo_name}...")
        Repo.clone_from(clone_url, repo_path)
        return repo_path
    
    return repo_path


def pull_repo(repo_name):
    repo_path = f"{BASE_REPO_DIR}/{repo_name}"
    repo = Repo(repo_path)
    origin = repo.remotes.origin
    origin.fetch()
    origin.pull()
    return repo_path


def get_changed_files(repo_name, old_commit, new_commit):
    repo_path = f"{BASE_REPO_DIR}/{repo_name}"
    repo = Repo(repo_path)
    diff = repo.git.diff("--name-only", old_commit, new_commit)
    return [f.strip() for f in diff.split("\n") if f.strip()]
