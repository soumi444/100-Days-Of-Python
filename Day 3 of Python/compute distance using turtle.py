import turtle

x1,y1 = eval(input("Enter x1 and y1 for Point 1 separated by commas:"))
x2,y2 = eval(input("Enter x2 and y2 for Point 2 separated by commas:"))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

turtle.penup()
turtle.goto(x1,y1)
turtle.down()
turtle.write("Point 1")

turtle.goto(x2,y2)
turtle.write("Point 2")

turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.down()
turtle.write(distance)

turtle.done()

