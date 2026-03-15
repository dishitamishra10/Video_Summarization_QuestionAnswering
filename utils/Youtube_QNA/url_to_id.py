import re

def get_videoID(url: str) -> str:
    pattern = r"/(\w{2,11}(?=\?))"
    matches = re.findall(pattern, url)

    return matches[0]