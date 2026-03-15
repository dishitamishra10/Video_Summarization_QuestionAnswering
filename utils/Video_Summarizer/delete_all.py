import os
import shutil

def cleanup_generated_files():
    """
    Deletes:
    - audio files from project root
    - frames folder from project root
    - __pycache__ from utils folder
    """

    # Directory of delete_all.py (utils folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Project root (one level above utils)
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    files_to_delete = [
        "audio.json",
        "audio.mp3",
        "audio.srt",
        "audio.tsv",
        "audio.txt",
        "audio.vtt"
    ]

    # Delete audio files from project root
    for file in files_to_delete:
        file_path = os.path.join(project_root, file)

        if os.path.isfile(file_path):
            os.remove(file_path)

    # Delete frames folder from project root
    frames_path = os.path.join(project_root, "frames")
    if os.path.isdir(frames_path):
        shutil.rmtree(frames_path)
