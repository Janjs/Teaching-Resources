import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

while True:
    window.update()

    pala_a = turtle.Turtle()
    pala_a.speed(0)
    pala_a.shape("square")
    pala_a.color("white")
    pala_a.shapesize(stretch_wid=5, stretch_len=1)
    pala_a.penup()
    pala_a.goto(-350, 0)

    pala_b = turtle.Turtle()
    pala_b.speed(0)
    pala_b.shape("square")
    pala_b.color("white")
    pala_b.shapesize(stretch_wid=5, stretch_len=1)
    pala_b.penup()
    pala_b.goto(350, 0)

    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("square")
    bola.color("white")
    bola.penup()
    bola.goto(0, 0)
