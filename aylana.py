import turtle as r
import colorsys as sm

r. tracer(5)
r.bgcolor("black")
r.pensize(2)
n = 500
h = 0
for i in range(500):
    for i in range(4):
        c = sm.hsv_to_rgb(h,1,1)
        h += 5/n
        r.color(c)
        r.circle(120+i*5,90)
        r.forward(200)
        r.left(800)
    r.right(10)
r.done

# from turtle import *
# from colorsys import *
# bgcolor("black")
# title("nimadur")
# width(5)
# speed(0)
# n = 250
# for i in range(n):
#     c = hsv_to_rgb(i/10,i/n,1)
#     fillcolor(c)
#     begin_fill()
#     rt(81)
#     circle(i*1.2,100)
#     end_fill()
#     rt(100)
# ht()
# done()
