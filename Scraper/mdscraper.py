"""
Markdown scraper
Converts markdown paragraphs to txt
""" 

import markdown # pip install markdown
import codecs
from bs4 import BeautifulSoup # pip install beautifulsoup4


def main():
    print("Hello world")
    fname = "./htmlTest.html"
    with open(fname, 'r', encoding="utf-8") as fp:
        # source_code = html_file.read() 
        print(fp.read())

# with open('htmlTest.html', 'r') as fp:
#     v = fp.read()

# def md_to_text(md):
#     html = markdown.markdown(md)
#     soup = BeautifulSoup(html, features='html.parser')
#     return soup.get_text()

main()