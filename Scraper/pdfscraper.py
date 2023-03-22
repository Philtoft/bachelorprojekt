import re
from PyPDF2 import PageObject, PdfReader
import PyPDF2


def processpdf(file) -> str:
    reader = PdfReader(file)
    print(f"PROCESSING PDF FILE '{file}'")
    print("Pages: %d\n" % len(reader.pages))
    text = extract_text(reader.pages)
    text = clean_text(text)
    return text

"""Extracts all text from pages"""
def extract_text(pages: list[PageObject]) -> str:
    text = []
    page: PyPDF2.PageObject
    for page in pages:
        text.append(page.extract_text())
    return "".join(text)

def clean_text(text: str) -> str:
    return remove_icons(text)

def remove_icons(text: str) -> str:
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)