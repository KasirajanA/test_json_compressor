import aiohttp
import asyncio
import json
import os

data = {
    "path": str(os.path.abspath("../resources/sample.json"))
}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8080/compress', json=data) as resp:
            print(resp.status)
            counter = 0
            json_data = ""
            while True:
                chunk = await resp.content.read(2000)
                counter += 1
                if not chunk:
                    break
                json_data += chunk.decode('utf-8')
            json_data = json.loads(json_data)
            print(json_data.keys())
            print("Total count of chunks: ", counter)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
