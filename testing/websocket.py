import asyncio
from websockets.asyncio.server import serve
from PIL import Image
import io

async def handler(websocket):
    print("connected")
    async for message in websocket:
        print("received")
        if isinstance(message, bytes):
            print("is image")
            Image.open(io.BytesIO(message)).show()
        else:
            print(message)

async def main():
    server = await serve(handler, "0.0.0.0", 8765, max_size=10*1024*1024)
    await server.serve_forever()

asyncio.run(main())