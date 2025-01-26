# Pong Game

Welcome to **Pong Game**, a modern take on the classic arcade game. This project features multiplayer gameplay, a server-client architecture, and smooth paddle controls, supporting both mouse and keyboard inputs.

---

## Features

- **Single Player Mode**: Play against an AI opponent.
- **Local Multiplayer**: 1v1 gameplay on a single machine.
- **Online Multiplayer**: Connect to a server and compete with players remotely.
- **Intuitive Controls**:
  - Keyboard (Arrow keys or `W`/`S`).
  - Mouse for precise paddle movement.
- **Server-Client Architecture**: Ensures seamless communication between players.

---


## Controls

- **Keyboard**:
  - `Arrow Up` / `W`: Move paddle up.
  - `Arrow Down` / `S`: Move paddle down.
- **Mouse**:
  - Move the mouse vertically to control the paddle.

---

## How It Works

### Architecture

- **Server**:
  - Manages the game state and synchronizes paddle and ball positions.
  - Broadcasts game state updates to all connected clients.

- **Client**:
  - Sends user input (keyboard/mouse) to the server.
  - Receives game state updates from the server and renders the game.

### Communication

- Built using **WebSockets** for real-time, low-latency communication.
- Messages between client and server are sent as JSON objects.

---

## Example Gameplay

### Single Player
- Compete against an AI that dynamically adjusts to your playstyle.

### Online Multiplayer
- Connect to the server, create a game, and invite your friends.
- Responsive paddle movements with minimal latency.

