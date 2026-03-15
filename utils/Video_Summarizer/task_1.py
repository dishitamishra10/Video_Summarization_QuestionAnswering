import os
import subprocess
from PIL import Image
import pytesseract


def video_frame_text(video_file):

    os.makedirs('frames', exist_ok=True)

    subprocess.run([
        "ffmpeg",
        "-i", video_file,
        "-vf", "fps=0.2",
        "frames/frame_%04d.jpg"
    ], check=True)

    folder_path = 'frames'
    all_text = ""
    valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(valid_ext):
            image_path = os.path.join(folder_path, file_name)

            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)

            all_text += text + '\n'

    return all_text