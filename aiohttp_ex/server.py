import os
from aiohttp import web

from utils import get_json_content


@web.middleware
async def compression_middleware(request, handler):
    response = await handler(request)
    response.enable_compression(web.ContentCoding.gzip)
    return response


async def handle(request):
    path = request.match_info.get("path", os.path.abspath("../resources/sample.json"))
    data = get_json_content(path)
    return web.json_response(data)


app = web.Application(middlewares=[compression_middleware])
app.add_routes([web.post('/compress', handle)])

if __name__ == '__main__':
    web.run_app(app, port=5000)
