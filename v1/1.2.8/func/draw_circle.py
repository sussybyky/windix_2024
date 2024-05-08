import turtle


def draw_circle(size, posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.circle(size)

    return
    # turtle.done()