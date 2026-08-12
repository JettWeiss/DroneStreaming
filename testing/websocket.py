import asyncio
from websockets.asyncio.server import serve
async def handler(websocket):
    async for message in websocket:
        print(message)

async def main():
    server = await serve(handler, "0.0.0.0", 8765)
    await server.serve_forever()

asyncio.run(main())