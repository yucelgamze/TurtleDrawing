import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("#DEFE28")
turtle_screen.title("🐢Turtle 🐢Python")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("DeepPink")
turtle_instance.fillcolor("DarkTurquoise")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

shrinkingSquare(150)
shrinkingSquare(120)
shrinkingSquare(90)
shrinkingSquare(60)
shrinkingSquare(30)
turtle.done()