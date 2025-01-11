import asyncio
import json
import secrets

from websockets import connect
from game.move_paddle import MovePaddle
from game.pong_game import PongGame
from network.events import Events

from websockets.asyncio.server import serve, broadcast

GAMES = {}

async def process_commands(websocket: connect, player_1: bool, name: str):
    async for message in websocket:
        print("Received command" + message)
        parsed_message = json.loads(message)
        if parsed_message["type"] == Events.MOVE.value:
            if player_1:
                GAMES[name][1] = MovePaddle(parsed_message["move"])
            else:
                GAMES[name][2] = MovePaddle(parsed_message["move"])

async def run_pong(name: str):
    print("Starting pong")
    game = PongGame(1280, 720)
    player_1_score = 0
    player_2_score = 0
    while True:
        connected, player_1_move, player_2_move = GAMES[name]
        paddle_1_position, paddle_2_position, ball_position, player_won = game.update(player_1_move, player_2_move)
        if player_won == 1:
            player_1_score += 1
            game = PongGame(1280, 720)
        elif player_won == 2:
            player_2_score += 1
            game = PongGame(1280, 720)
        broadcast(connected, json.dumps({
            "type": Events.STATE.value,
            "paddle_1_position": json.dumps(paddle_1_position, default=lambda o: o.__dict__),
            "paddle_2_position": json.dumps(paddle_2_position, default=lambda o: o.__dict__),
            "ball_position": json.dumps(ball_position, default=lambda o: o.__dict__),
            "player_1_score": player_1_score,
            "player_2_score": player_2_score
        }))
        await asyncio.sleep(1 / 60)

async def start(websocket):
    print("Starting game")
    game_name = secrets.token_urlsafe(12)
    GAMES[game_name] = [[websocket], MovePaddle.NONE, MovePaddle.NONE]
    print("Created game with key: " + game_name)
    try:
        await websocket.send(json.dumps({"type": Events.CREATED.value, "name": game_name}))
        await process_commands(websocket, True, game_name)
    finally:
        del GAMES[game_name]

async def join(websocket, name):
    print("Joining game: " + name)
    try:
        connected, _, _ = GAMES[name]
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
        asyncio.create_task(run_pong(name))
        await process_commands(websocket, False, name)
    finally:
        connected.remove(websocket)

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
