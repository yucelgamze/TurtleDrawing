import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#DEFE28")
#drawing_board.bgcolor("DeepPink")
#drawing_board.bgcolor("DarkTurquoise")
drawing_board.title("Python Turtle 🐢")


#square
'''
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
'''

'''
#star
turtle_instance_2 = turtle.Turtle()
for i in range(5):
    turtle_instance_2.forward(300)
    turtle_instance_2.left(144)
'''

#polygon
turtle_instance_2 = turtle.Turtle()
num_sides = 8
angle = 360.0 / num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance_2.left(angle)
    turtle_instance_2.forward(side_length)

turtle.done()   # this way window doesn't close when its job done.