import re

import pymupdf


def clean_text(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    return text.strip()


def extract_text_from_pdf(file_path: str) -> str:
    pages = []

    with pymupdf.open(file_path) as doc:
        for page in doc:
            pages.append(page.get_text())

    return clean_text("\n\n".join(pages))
