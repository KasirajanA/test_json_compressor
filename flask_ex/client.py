import requests
import json
import os

url = "http://127.0.0.1:5000/compress_stream"

data = {
    "path": str(os.path.abspath("../resources/sample.json"))
}
headers = {
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/json'
}

with requests.Session() as s:
    with s.post(url, headers=headers, json=data, stream=True) as response:
        counter = 0
        json_data = ""
        chunks = response.iter_content(2000)
        for chunk in chunks:
            counter += 1
            if not chunk:
                break
            json_data += chunk.decode('utf-8')
        json_data = json.loads(json_data)
        print(json_data.keys())
        print("Total count of chunks: ", counter)

