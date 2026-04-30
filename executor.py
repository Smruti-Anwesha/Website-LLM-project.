import os

def save_files(html, css):
    os.makedirs("output", exist_ok=True)

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    with open("output/style.css", "w", encoding="utf-8") as f:
        f.write(css)

    print("Website files saved in 'output' folder")