## Pong Game - How it works

This is a classic **Pong Game** built with Python's Turtle module. Two players control paddles to hit a ball and score points.

### Project files

- `Paddle.py` – controls paddle movement
- `Ball.py` – handles ball movement and bouncing
- `Scoreboard.py` – tracks and displays scores
- `main.py` – runs the main game loop

### What is used

- `turtle` module: for graphics and animation
- `time` module: to control game speed
- class inheritance: each game object inherits from Turtle

### How it works

1. Two paddles (left and right) are placed on opposite sides
2. Ball moves around the screen
3. Each player tries to hit the ball with their paddle
4. If ball hits top or bottom wall → bounces
5. If ball hits paddle → bounces and speeds up
6. If ball passes a paddle → other player gets 1 point
7. Ball resets to center after each point

### Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| Left (Blue side) | W | S |
| Right (Red side) | R | F |

### Game rules

- First to score more points wins
- Ball gets faster each time it hits a paddle
- Game continues forever until you close the window
- Scores reset when you restart the game

### Features

- Ball speed increases gradually (makes game harder)
- Smooth paddle movement
- Clean black and white design

---

Classic arcade fun for two players!
