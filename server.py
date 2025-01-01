import asyncio
import json
from network.events import Events

from websockets.asyncio.server import serve

async def start(websocket):
    print("Starting game")

async def join(websocket, name):
    print("Joining game: " + name)

async def handler(websocket):
    message = await websocket.recv()
    event = json.loads(message)

    if "type" not in event:
        return

    if event["type"] == Events.JOIN.value:
        await join(websocket, event["name"])
    elif event["type"] == Events.CREATE.value:
        await start(websocket)

async def main():
    async with serve(handler, "", 8001):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
