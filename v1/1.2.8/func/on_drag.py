import turtle


def on_drag(x, y):
    turtle.speed(100)
    turtle.ondrag(None)
    turtle.goto(x, y)
    turtle.ondrag(on_drag)
    return
