import turtle

def draw_square(some_turtle):
    for x in range(0,4):
         some_turtle.forward(100)
         some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0,3):
         some_turtle.forward(100)
         some_turtle.right(120)
    
def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")

     #Create the turtle brad - Draws a square
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    loop_count = 100
    for j in range(0,loop_count):
        draw_square(brad)
        brad.right(360.0/loop_count)

    """
     #Create a turtle angie - Draws a square
    
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    # Create a turtle triangle - Draws a triangle
    triangle = turtle.Turtle()
    draw_triangle(triangle)
    
     """
         
    window.exitonclick()





draw_art()
