from turtle import Turtle, Screen

def draw_branch(turtle: Turtle, length, angle, start_point=(0,0)):
    
    turtle.up()
    turtle.goto(start_point)
    turtle.down()
    turtle.setheading(angle)
    turtle.forward(length)

def draw_tree(turtle, length, angle, start_point=(0,0), order=3):
    
    if order == 0:
        draw_branch(turtle, length, angle, start_point)
    else:
        draw_branch(turtle, length, angle, start_point)
        new_pos = turtle.pos()
        draw_tree(turtle, length/(2**0.5), angle + 45, start_point=new_pos, order=order-1)
        draw_tree(turtle, length/(2**0.5), angle - 45, start_point=new_pos, order=order-1)
           

if __name__ == "__main__":
    turtle = Turtle()
    turtle.hideturtle()
    window = Screen()
    window.bgcolor("white")
    
    start_point = (0, 0)
    draw_tree(turtle, 100, 90, start_point, order=8)
    
    window.mainloop()