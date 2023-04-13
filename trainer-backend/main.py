import json
from flask import Flask, request, Response
from flask_cors import CORS
import requests
import wikiscraper as ws
from bs4 import BeautifulSoup as bs4

ws.lang("en")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    wikiURL = request.args.get('url')

    if wikiURL is None:
        return Response('{"error": "No URL provided"}', status=400, mimetype='application/json')
    
    # Check if article exists
    wiki_article_scraped = get_wiki_data(wikiURL)
    
    return json.dumps({ 'article': wiki_article_scraped })

def get_wiki_data(url):
    
    response = requests.get(url=url)

    soup = bs4(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    print(title.string)

    return "result"
    
if __name__ == '__main__':
    app.run(debug=True)
                       
# app.run()