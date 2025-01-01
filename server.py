import asyncio
import json
import secrets
from network.events import Events

from websockets.asyncio.server import serve

GAMES = {}

async def start(websocket):
    print("Starting game")
    game_key = secrets.token_urlsafe(12)
    GAMES[game_key] = [websocket]
    print("Created game with key: " + game_key)

async def join(websocket, name):
    print("Joining game: " + name)
    try:
        connected = GAMES[name]
    except KeyError:
        print("Game not found")
        #await error(websocket, "Game not found.")
        return

    if len(connected) >= 2:
        print("Game already has two players")
        return

    connected.append(websocket)
    print("Player added to the game")

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
