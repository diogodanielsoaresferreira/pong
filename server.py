import asyncio
import json
import secrets
from network.events import Events

from websockets.asyncio.server import serve, broadcast

GAMES = {}

async def process_commands(websocket):
    async for message in websocket:
        print("Received command" + message)
        parsed_message = json.loads(message)

async def run_pong(connected):
    print("Starting pong")
    while True:
        broadcast(connected, json.dumps({"type": Events.STATE.value}))
        await asyncio.sleep(1 / 60)

async def start(websocket):
    print("Starting game")
    game_name = secrets.token_urlsafe(12)
    GAMES[game_name] = [websocket]
    print("Created game with key: " + game_name)
    try:
        await websocket.send(json.dumps({"type": Events.CREATED.value, "name": game_name}))
        await process_commands(websocket)
    finally:
        pass
        #del GAMES[game_name]

async def join(websocket, name):
    print("Joining game: " + name)
    try:
        connected = GAMES[name]
    except KeyError:
        print("Game " + name + " not found. Games are: " + str(GAMES.keys()))
        await websocket.send(json.dumps({"type": Events.ERROR.value, "message": "Game " + name + " not found"}))
        return

    if len(connected) >= 2:
        print("Game already has two players")
        await websocket.send(json.dumps({"type": Events.ERROR.value, "message": "Game already has two players"}))
        return

    connected.append(websocket)
    print("Player added to the game")
    broadcast(connected, json.dumps({"type": Events.JOINED.value}))
    try:
        asyncio.create_task(run_pong(connected))
        await process_commands(websocket)
    finally:
        pass
        #connected.remove(websocket)

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
