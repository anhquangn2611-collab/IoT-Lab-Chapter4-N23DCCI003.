from sense_emu import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

snake = [[3, 3]]
food = [random.randint(0, 7), random.randint(0, 7)]
direction = "right"
score = 0

GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]

def move(event):
    global direction
    if event.action == "pressed":
        if event.direction == "up" and direction != "down":
            direction = "up"
        elif event.direction == "down" and direction != "up":
            direction = "down"
        elif event.direction == "left" and direction != "right":
            direction = "left"
        elif event.direction == "right" and direction != "left":
            direction = "right"

sense.stick.direction_any = move
print("=> Game bat dau! Dung Joystick tren Emulator de dieu khien.")

try:
    while True:
        head = list(snake[0])
        if direction == "up": head[1] -= 1
        elif direction == "down": head[1] += 1
        elif direction == "left": head[0] -= 1
        elif direction == "right": head[0] += 1
            
        if head[0] < 0 or head[0] > 7 or head[1] < 0 or head[1] > 7 or head in snake:
            print(f"=> Game Over! Diem cua ban: {score}")
            sense.show_message(f"Score: {score}", text_colour=RED)
            break
            
        snake.insert(0, head)
        if head == food:
            score += 1
            while food in snake:
                food = [random.randint(0, 7), random.randint(0, 7)]
        else:
            snake.pop()
            
        sense.clear()
        sense.set_pixel(food[0], food[1], BLUE)
        for segment in snake:
            sense.set_pixel(segment[0], segment[1], GREEN)
        time.sleep(0.4)
except KeyboardInterrupt:
    sense.clear()