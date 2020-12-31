from PIL import Image
import requests
import os
import hashlib

def get(url, path):
    r = requests.get(url, stream=True, allow_redirects=True, timeout=30)
    r.raise_for_status()
    r.raw.decode_content = True

    path = os.path.join(path, hashlib.sha1(url.encode()).hexdigest()[:5]+".jpg")
    with Image.open(r.raw) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(path)
    r.close()

def download(url_file, path="images/"):
    with open(url_file, "r") as f:
        for url in f.read().split("\n"):
            try:
                get(url, path=path)
            except Exception as e:
                print(e)

download("assets/dark.txt")
download("assets/bright.txt")