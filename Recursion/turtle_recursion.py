__author__ = 'bhushan'

import turtle

my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    my_turtle = turtle.Turtle()
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


#draw_spiral(my_turtle, 100)

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(40, t)

main()
my_win.exitonclick()
