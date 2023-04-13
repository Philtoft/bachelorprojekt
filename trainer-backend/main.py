import json
from flask import Flask, request, Response
from flask_cors import CORS
import wikiscraper as ws

ws.lang("en")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    slug = request.args.get('url')

    if slug is None:
        return Response('{"error": "No URL provided"}', status=400, mimetype='application/json')
    
    # Check if article exists
    wiki_article_abstract = get_wiki_data(slug)
    article_merged = merge_abstract_sentences(wiki_article_abstract)
    
    return json.dumps({ 'article': article_merged })

def get_wiki_data(slug):
    ws_result = ws.searchBySlug(slug)
    return ws_result.getAbstract()
    
if __name__ == '__main__':
    app.run(debug=True)
                       
# app.run()