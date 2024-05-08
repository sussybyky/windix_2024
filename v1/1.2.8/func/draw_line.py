import turtle


def draw_line(size, facing, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(0, 0)
    turtle.pendown()

    if facing == "up":
        turtle.goto(0, size)
    elif facing == "down":
        turtle.goto(0, -size)
    elif facing == "right":
        turtle.goto(size, 0)
    elif facing == "left":
        turtle.goto(-size, 0)
    else:
        print("Wrong input! Try again.")
        return
