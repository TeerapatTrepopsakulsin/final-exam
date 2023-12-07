import turtle
import random

class Draw:
    def __init__(self, num_sides, reduction_ratio, location):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = location
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = reduction_ratio

    def polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def reposition(self):
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def get_new_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def get_new_position(self):
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]


choice = input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: ')
if choice == '1':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(3, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
    turtle.done()
if choice == '2':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(4, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
    turtle.done()
if choice == '3':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(5, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
    turtle.done()
if choice == '4':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        num_side = random.randint(3, 5)
        a = Draw(num_side, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
    turtle.done()
if choice == '5':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(3, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
        a.reposition()
        for i in range(2):
            a.size *= a.reduction_ratio
            a.polygon()
    turtle.done()
if choice == '6':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(4, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
        a.reposition()
        for i in range(2):
            a.size *= a.reduction_ratio
            a.polygon()
    turtle.done()
if choice == '7':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        a = Draw(5, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
        a.reposition()
        for i in range(2):
            a.size *= a.reduction_ratio
            a.polygon()
    turtle.done()
if choice == '8':
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    for _ in range(30):
        num_side = random.randint(3, 5)
        a = Draw(num_side, 0.618, [0, 0])
        a.get_new_position()
        a.polygon()
        a.reposition()
        for i in range(2):
            a.size *= a.reduction_ratio
            a.polygon()
    turtle.done()
