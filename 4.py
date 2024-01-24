import turtle
import time

# Function to draw the clock face
def draw_clock_face():
    # Draw the outer circle
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(200)

    # Draw the hour marks
    for _ in range(12):
        turtle.penup()
        turtle.goto(0, 160)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.goto(0, -180)
        turtle.right(30)

# Function to update the time on the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    turtle.clear()
    draw_clock_face()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write(current_time, align="center", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.write("Press 'q' to quit.", align="center", font=("Arial", 12, "normal"))
    turtle.hideturtle()
    turtle.update()

# Initialize the Turtle screen
screen = turtle.Screen()
screen.title("Clock")
screen.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# Draw the clock face initially
draw_clock_face()

# Update the clock every second
while True:
    update_clock()
    time.sleep(1)

# Close the Turtle graphics window when the user presses 'q'
def close_window():
    screen.bye()

screen.onkey(close_window, 'q')
screen.listen()
screen.mainloop()
