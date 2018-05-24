import aiohttp
from quart import Quart, Response, jsonify

app = Quart(__name__)

@app.route('/json')
async def test_json() -> Response:
    """Returns a test remote JSON payload"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/json') as response:
            data = await response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8000)
