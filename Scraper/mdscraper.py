"""
Markdown scraper
Converts markdown paragraphs to txt
""" 

from markdown import markdown # pip install markdown
import codecs
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re


# def main():
#     print("Hello world")
#     fname = "./htmlTest.html"
#     with open("./htmlTest2.html", 'r', encoding="utf-8") as fp:
#         source_code = html_file.read() 
#         print(fp.read())

# with open('htmlTest.html', 'r') as fp:
#     v = fp.read()

# def md_to_text(md):
#     html = markdown.markdown(md)
#     soup = BeautifulSoup(html, features='html.parser')
#     return soup.get_text()

# main()


# def markdown_to_text():
#     """ Converts a markdown string to plaintext """

#     with open("./test.md", 'r') as md:

#         # md -> html -> text since BeautifulSoup can extract text cleanly
#         html = markdown(md)

#         # remove code snippets
#         html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
#         html = re.sub(r'<code>(.*?)</code >', ' ', html)

#         # extract text
#         soup = BeautifulSoup(html, "html.parser")
#         text = ''.join(soup.findAll(text=True))

#         return text

# markdown_to_text()

# def htmlToTxt():
#     with open ("./htmlTest.html", 'r') as htmlString:
#         # html = markdown(htmlString)
#         text = join(BeautifulSoup(htmlString).findAll(text=True))
#         print(text)

# htmlToTxt()
# def test():
#     html = markdown.markdown(open("test.md").read())
#     print("".join(BeautifulSoup(html).findAll(text=True)))

# test()

def cleanHtml(htmlDoc):
    with open (htmlDoc, 'r', encoding="utf-8"):
        # Regex for Formulas: ((<ul).*(class="katex").*(<\/ul>))*
        # Regex for billeder + fomulas: (((<ul).*(class="katex").*(<\/ul>))*((<img).*\/>)*)* 
        # Regex for 

def test2():
    with open ("./htmlTest.html", 'r', encoding="utf-8") as html:
        # Initialize the object with the document
        soup = BeautifulSoup(html, "html.parser")
        
        # Get the whole body tag
        tag = soup.body

        combined_string = ""
        
        # Print each string recursively
        for string in tag.strings:
            print(string)
            combined_string += string
        
        with open("test.txt", "w", encoding="utf-8") as text_file:
            text_file.write(combined_string)

        
test2()