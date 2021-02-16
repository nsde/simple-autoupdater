import os
import requests

debug_mode = False

def get(url):
    response = requests.get(url)
    return response.text

def apply(path, content):
    cwd = os.getcwd()
    open(cwd + "\\" + path, "w").write(content)

def update(from_url, to_path):
    content = get(from_url)
    apply(path=to_path, content=content)

if __name__ == "__main__": # Demo
    update(from_url="https://raw.githubusercontent.com/nsde/simple-autoupdater/main/demo/new.txt", to_path="demo\old.txt")