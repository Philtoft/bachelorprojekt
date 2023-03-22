
import sys
from pdfquery import pdfquery
from pdfscraper import processpdf

def main():
    args = sys.argv[1:]

    pdf = pdfquery.PDFQuery(args[0])
    pdf.load()
    pdf.tree.write('pdfXML.txt', pretty_print = True)

    if len(args) == 1:
        if (args[0].endswith(".pdf")):
            text = processpdf(args[0])
            save_scrape(args[0], text)
        else:
            print("Error: '%s' is not a pdf-file" % (args[0]))
    else:
        print("Error: Please specify a pdf-file")

def save_scrape(filename: str, text: str):
    outputname = filename.replace("pdf", "txt")
    with open(outputname, "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()