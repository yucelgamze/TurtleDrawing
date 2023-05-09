import turtle

turtle_screen = turtle.Screen()
turtle_screen.title("🐢Turtle Python🐢")
turtle_screen.bgcolor("#DEFE28")

turtle_instance = turtle.Turtle()
turtle_instance.color("DeepPink")
turtle_instance.speed(30)

turtle_colors = ["DeepPink", "DarkTurquoise", "DarkOrchid", "HotPink", "firebrick4", "gray20"]

for i in range(20):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
turtle.mainloop()
#turtle.done()