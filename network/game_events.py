import json
import pygame
from domain.ball_position import BallPosition
from domain.paddle_position import PaddlePosition
from game.move_paddle import MovePaddle
from network.events import Events
from websockets.asyncio.client import connect
from player.keyboard_arrow_mouse_player import KeyboardArrowAndMousePlayer
from ui.screen import Screen

async def create_online_game(screen: pygame.surface, server_uri: str):
    event = {"type": Events.CREATE.value}
    print("Creating game")
    async with connect(server_uri) as websocket:
        await websocket.send(json.dumps(event))
        created = False
        while not created:
            message = await websocket.recv()
            json_message = json.loads(message)
            if ("type" in json_message and json_message["type"] == Events.CREATED.value):
                created = True
        await run_game(screen, websocket, True)

async def join_online_game(screen: pygame.surface, server_uri: str, game_name: str):
    event = {"type": Events.JOIN.value, "name": game_name}
    print("Joining game: " + game_name)
    async with connect(server_uri) as websocket:
        await websocket.send(json.dumps(event))
        joined = False
        while not joined:
            message = await websocket.recv()
            json_message = json.loads(message)
            if ("type" in json_message and json_message["type"] == Events.JOINED.value):
                joined = True
        await run_game(screen, websocket, False)

async def run_game(screen: pygame.surface, websocket: connect, player_1: bool):
    game_screen = Screen(screen)
    player = KeyboardArrowAndMousePlayer()
    async for message in websocket:
        json_message = json.loads(message)
        if ("type" in json_message and json_message["type"] == Events.STATE.value):
            paddle_1_position = PaddlePosition.from_json(json.loads(json_message["paddle_1_position"]))
            paddle_2_position = PaddlePosition.from_json(json.loads(json_message["paddle_2_position"]))
            ball_position = BallPosition.from_json(json.loads(json_message["ball_position"]))
            player_1_score = json_message["player_1_score"]
            player_2_score = json_message["player_2_score"]
            game_screen.draw(paddle_1_position, paddle_2_position, ball_position, player_1_score, player_2_score)
            if player_1:
                move = player.calculate_move(paddle_1_position, ball_position)
            else:
                move = player.calculate_move(paddle_2_position, ball_position)
            if move == MovePaddle.UP or move == MovePaddle.DOWN:
                await websocket.send(json.dumps({"type": Events.MOVE.value, "move": MovePaddle.UP.value}))
