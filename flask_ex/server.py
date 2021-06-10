import os
import json

from flask import Flask, request, jsonify, Response
from flask_compress import Compress

from utils import get_json_content

json_encoder = json.JSONEncoder()
app = Flask(__name__)
Compress(app)


@app.route("/compress", methods=["POST"])
def handle():
    content = request.json
    path = content.get("path", os.path.abspath("../resources/sample.json"))
    data = get_json_content(path)
    return jsonify(data)


@app.route("/compress_stream", methods=["POST"])
def stream():
    content = request.json
    path = content.get("path", os.path.abspath("../resources/sample.json"))
    data = get_json_content(path)

    def generate():
        counter = 0
        for item in json_encoder.iterencode(data):
            yield item
            # counter += 1
            # if counter >= 100:
            #     break
    return Response(generate(), content_type='application/json')


if __name__ == "__main__":
    app.run()
