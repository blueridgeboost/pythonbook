# import turtle           # Imports the turtle library

# turtle.clearscreen()           # Remove drawings from previous runs.
# turtle.setup(200, 100)         # Sets the dimensions of the viewing window.

# shelly = turtle.Turtle()       # Create a turtle, assign to shelly

# shelly.forward(50)             # Tell shelly to move forward by 50 units
# shelly.left(90)                # Tell shelly to turn left by 90 degrees
# shelly.forward(30)             # Complete the second side of a rectangle

# turtle.mainloop()              # Keep the window from closing

# import turtle

# turtle.clearscreen() 
# turtle.setup(200,200)

# turtle.bgcolor("lightgreen")    # Set the background color

# shelly = turtle.Turtle()
# shelly.color("blue")		    # Tell shelly to change her color
# shelly.pensize(3)               # Tell shelly to set her pen width

# shelly.forward(50)
# shelly.left(120)
# shelly.forward(50)
# turtle.mainloop() 

# import turtle

# turtle.clearscreen() 
# turtle.setup(200,200)
# turtle.bgcolor("lightgreen")


# tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)

# alex = turtle.Turtle()       # Create alex

# # Make tess draw an equilateral triangle
# tess.forward(80)             
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)               # Complete the triangle

# tess.right(180)              # Turn tess around
# tess.forward(80)             # Move her away from the origin

# # Make alex draw a square
# alex.forward(50)             
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# turtle.mainloop() 

# import turtle

# turtle.clearscreen() 
# turtle.setup(200,200)

# alex = turtle.Turtle() 

# for i in [0, 1, 2, 3]:       # Draw the four sides of the square
#     alex.forward(50)
#     alex.left(90)

# turtle.mainloop()

# import turtle

# turtle.clearscreen() 
# turtle.setup(200,200)

# alex = turtle.Turtle()       # Create alex

# for c in ["yellow", "red", "purple", "blue"]:
#     alex.color(c)
#     alex.forward(50)
#     alex.left(90)

# turtle.mainloop()

# import turtle

# turtle.clearscreen() 
# turtle.setup(200,200)

# shelly = turtle.Turtle()       # Create shelly

# shelly.penup()
# shelly.forward(100)     # This moves shelly, but no line is drawn
# shelly.pendown()

# turtle.mainloop()

# import turtle

# turtle.clearscreen()        # Creates a playground for turtles
# turtle.setup(200, 100) 

# shelly = turtle.Turtle()    # Create a turtle, assign to shelly
# shelly.shape("turtle")      # Shape shelly to look like a turtle

# shelly.forward(50)          # Tell shelly to move forward by 50 units
# shelly.left(90)             # Tell shelly to turn by 90 degrees
# shelly.forward(30)          # Complete the second side of a rectangle

# turtle.mainloop()

# import turtle

# turtle.clearscreen()        # Creates a playground for turtles
# turtle.setup(600, 600) 
# turtle.bgcolor("lightgreen")

# shelly = turtle.Turtle()
# shelly.shape("turtle")
# shelly.color("blue")

# shelly.penup()
# size = 20
# for _ in range(30):
#     shelly.stamp()             # Leave an impression on the canvas
#     size = size + 3            # Increase the size on every iteration
#     shelly.forward(size)       # Move shelly along
#     shelly.right(24)           #  ...  and turn her

# turtle.mainloop()

# import turtle

# turtle.clearscreen()
# turtle.setup(200,200)        # Creates a playground for turtles
# shelly = turtle.Turtle()    # Create a turtle, assign to shelly

# shelly.forward(50)          # Tell shelly to move forward by 50 units
# shelly.left(90)             # Tell shelly to turn by 90 degrees
# shelly.forward(30)          # Complete the second side of a rectangle

# shelly.write("Hi there!")   # Write a message

# turtle.mainloop()

# import turtle

# turtle.clearscreen()
# turtle.setup(200,200)        # Creates a playground for turtles
# shelly = turtle.Turtle()      # Create shelly

# shelly.begin_fill()           # Start of the region to fill
# for i in range(4):            # Draw the four sides of the square
#     shelly.forward(50)
#     shelly.left(90)
# shelly.end_fill()             # Fill the region

# turtle.mainloop()

# import turtle

# turtle.clearscreen()
# turtle.setup(200,200)        # Creates a playground for turtles
# shelly = turtle.Turtle()      # Create shelly
# shelly.color("blue")          # Set pen color to blue
# shelly.fillcolor("red")       # Set fill color to red

# shelly.begin_fill()           # Start of the region to fill
# for i in range(4):            # Draw the four sides of the square
#     shelly.forward(50)
#     shelly.left(90)
# shelly.end_fill()             # Fill the region

# turtle.mainloop()

# import turtle

# xs = [48, 117, 200, 240, 160, 260, 220] # our data

# def draw_bar(t, h):
#     """ Get turtle t to draw one bar, of height h. """
#     t.left(90)
#     t.forward(h)          # Draw up the left side
#     t.right(90)
#     t.forward(40)         # Width of bar, along the top
#     t.right(90)
#     t.forward(h)          # And down again!

#     t.left(90)            # Put the turtle facing the way we found it.
#     t.forward(10)         # Leave small gap after each bar

# turtle.clearscreen()  
# turtle.setup(400, 400)
# turtle.bgcolor("lightgreen")

# shelly = turtle.Turtle()
# shelly.penup()
# shelly.goto(-190, -190)
# shelly.pendown()
# shelly.color("blue")
# shelly.fillcolor("darkblue")

# for v in xs:             
#     draw_bar(shelly, v)

# turtle.mainloop()

# import turtle

# xs = [48, 117, 200, 240, 160, 260, 220] # our data

# def draw_bar(t, h):
#     """ Get turtle t to draw one bar, of height h. """
#     t.begin_fill()                # Start of the fill area
#     t.left(90)
#     t.forward(h)                  # Draw up the left side
#     t.write("  " + str(h))        # Write the data
#     t.right(90)
#     t.forward(40)                 # Width of bar, along the top
#     t.right(90)
#     t.forward(h)                  # and down again!
#     t.left(90)                    # Put the turtle facing the way started
#     t.end_fill()                  # Fill in the bar
#     t.forward(10)                 # Leave small gap after each bar

# turtle.clearscreen()  
# turtle.setup(400, 400)
# turtle.bgcolor("lightgreen")

# shelly = turtle.Turtle()
# shelly.penup()
# shelly.goto(-190, -190)
# shelly.pendown()
# shelly.color("blue")
# shelly.fillcolor("darkblue")

# for v in xs:              # Draw a bar for each number in the data
#     draw_bar(shelly, v)

# turtle.mainloop()

import turtle

turtle.clearscreen()
turtle.setup(200,200)

turtle.colormode(255)       #  r, g, b values of color triples have to be in the range 0..255. 
turtle.bgcolor(255, 0, 255) # ("lightgreen")

leonardo = turtle.Turtle()       # Create Leonardo, a skilled turtle leader
leonardo.color("darkgreen")
leonardo.pensize(5)

raphael = turtle.Turtle()       # Create Raphael, a strong turtle
raphael.color("red")
raphael.pensize(3)

donatello = turtle.Turtle()      # Create Donatello, the smartest turtle
donatello.color("purple")
donatello.pensize(3)

leonardo.forward(80)             # Make leonardo draw an equilateral triangle
leonardo.left(120)
leonardo.forward(80)
leonardo.left(120)
leonardo.forward(80)
leonardo.left(120)               # Complete the triangle

leonardo.right(180)              # Turn leonardo around
leonardo.forward(80)             # Move her away from the origin

raphael.forward(50)              # Make raphael draw a square
raphael.left(90)
raphael.forward(50)
raphael.left(90)
raphael.forward(50)
raphael.left(90)
raphael.forward(50)
raphael.left(90)

turtle.mainloop()