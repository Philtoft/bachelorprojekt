import json
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    url = request.args.get('url')
    return json.dumps({ 'URL': url })

                       
if __name__ == '__main__':
    app.run(debug=True)
                       
# app.run()