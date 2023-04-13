import json
from flask import Flask, request, Response
from flask_cors import CORS
import requests
import wikiscraper as ws
from bs4 import BeautifulSoup as bs4

ws.lang("en")

app = Flask(__name__)
CORS(app)

# Should return link with the first 10 articles from the search that can be scraped
@app.route('/')
def index():
    wikiSlug = request.args.get('slug')

    if wikiSlug is None:
        return Response('{"error": "No URL provided"}', status=400, mimetype='application/json')
    
    # Check if article exists
    links = get_first_10_links(wikiSlug)
    
    return json.dumps({ 'links': links })

def get_first_10_links(slug):

    url = "https://en.wikipedia.org/wiki/" + slug
    
    response = requests.get(url=url)

    soup = bs4(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    # Get first 10 links
    # remove sidebar table
    for element in soup.find(class_="sidebar sidebar-collapse nomobile nowraplinks hlist"):
        element.decompose()
    
    first_links = soup.find(id="mw-content-text").find_all("a")

    links = []

    for link in first_links:
        # Ignores everything in the class "hatnote navigation-not-searchable" and only gets links that start with "/wiki/"
        if link.find_parent(class_="hatnote navigation-not-searchable") is None and link.has_attr('href') and link['href'].startswith("/wiki/") and len(links) < 10:
            links.append(link['href'])

    return links
    
if __name__ == '__main__':
    app.run(debug=True)
                       
# app.run()