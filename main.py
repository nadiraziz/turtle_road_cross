from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

turtle = Turtle()
turtle.hideturtle()


screen.onkey(player.go_up, "Up")
is_gam_on = True
while is_gam_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_gam_on = False
            scoreboard.game_over()

    if player.is_at_finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_increase()


screen.exitonclick()
