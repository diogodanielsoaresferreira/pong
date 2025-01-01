import json
from network.events import Events
from websockets.asyncio.client import connect

async def create_online_game(server_uri: str):
    event = {"type": Events.CREATE.value}
    print("Creating game")
    async with connect(server_uri) as websocket:
        await websocket.send(json.dumps(event))

async def join_online_game(server_uri: str, game_name: str):
    event = {"type": Events.JOIN.value, "name": game_name}
    print("Joining game: " + game_name)
    async with connect(server_uri) as websocket:
        await websocket.send(json.dumps(event))
