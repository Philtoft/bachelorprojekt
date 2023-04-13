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
    
    return json.dumps({ 'article': wiki_article_abstract })

def get_wiki_data(url):
    ws_result = ws.searchBySlug(url)
    print(ws_result)
    return ws_result.getAbstract()
    

                       
if __name__ == '__main__':
    app.run(debug=True)
                       
# app.run()