import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)

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
bola.dx = 2
bola.dy = 2

def pala_a_up():
    y = pala_a.ycor()
    y = y + 20
    pala_a.sety(y)

def pala_a_down():
    y = pala_a.ycor()
    y = y - 20
    pala_a.sety(y)

def pala_b_up():
    y = pala_b.ycor()
    y = y + 20
    pala_b.sety(y)

def pala_b_down():
    y = pala_b.ycor()
    y = y - 20
    pala_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(pala_a_up, "w")
window.onkeypress(pala_a_down, "s")
window.onkeypress(pala_b_up, "Up")
window.onkeypress(pala_b_down, "Down")

# marcador
marcador_a = 0
marcador_b = 0
pen.write("Jugador A: "+str(marcador_a)+" Jugador B: "+str(marcador_b)+"", align="center", font=("Courier", 24, "normal"))

while True:
    window.update()

    # moure bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        marcador_a += 1
        pen.clear()
        pen.write("Jugador A: " + str(marcador_a) + " Jugador B: " + str(marcador_b) + "", align="center",
                  font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        marcador_b += 1
        pen.clear()
        pen.write("Jugador A: " + str(marcador_a) + " Jugador B: " + str(marcador_b) + "", align="center",
                  font=("Courier", 24, "normal"))

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < pala_b.ycor() + 50 and bola.ycor() > pala_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < pala_a.ycor() + 50 and bola.ycor() > pala_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1




