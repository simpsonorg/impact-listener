import os

base_folder = 'impact-listener'
structure = {
    'app': ['main.py', 'repo_sync.py', 'embeddings.py', 'db.py', 'models.py'],
    '': ['requirements.txt', 'Dockerfile', 'README.md']
}

# Create base folder
os.makedirs(base_folder, exist_ok=True)

# Create subfolders and files
for folder, files in structure.items():
    folder_path = os.path.join(base_folder, folder) if folder else base_folder
    if folder:  # create subfolder
        os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'w') as f:
            pass  # create empty file
