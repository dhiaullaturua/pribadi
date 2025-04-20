import turtle
import random

# Fungsi untuk menggambar kelopak bunga
def draw_petal(t):
    angle = 60
    t.color(random.choice(['red', 'blue', 'yellow', 'purple', 'orange', 'pink']))
    t.begin_fill()
    t.circle(100, angle)
    t.left(120)
    t.circle(100, angle)
    t.left(120)
    t.end_fill()

# Fungsi untuk menggambar bunga
def draw_flower(t, petal_count):
    for _ in range(petal_count):
        draw_petal(t)
        t.left(360 / petal_count)

# Fungsi untuk menggambar batang
def draw_stem(t):
    t.color("green")
    t.right(90)
    t.pensize(10)
    t.forward(200)

# Fungsi utama
def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")

    t = turtle.Turtle()
    t.speed(10)

    draw_flower(t, 10)  # Menggambar bunga dengan 10 kelopak
    draw_stem(t)        # Menggambar batang

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()