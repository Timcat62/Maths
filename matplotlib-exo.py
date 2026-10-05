from pylab import *
from matplotlib import *

def triangle():
    xlim(0, 10)
    ylim(0, 10)
    x = [2, 5, 8, 2]
    y = [2, 8, 2, 2]
    plot(x, y, '-*r')
    show()

triangle()


def rectangle():
    xlim(0, 10)
    ylim(0, 10)
    x = [3, 3, 7, 7, 3]
    y = [3, 7, 7, 3, 3]
    plot(x, y, '-*r')
    show()

rectangle()


def pointLine():
    xlim(0, 20)
    ylim(2.0, 4.0)
    for i in range(10):
        x = 5 + i
        y = 3
        plot(x, y, '-*b')
    show()

pointLine()


def pointLine2():
    xlim(0, 20)
    ylim(2.0, 6.0)
    for i in range(10):
        x = 5 + i
        y = 3.0
        plot(x, y, '-*r')
    for i in range(10):
        x = 5 + i
        y = 5.0
        plot(x, y, '-*b')
    show()

pointLine2()


def pointLine3():
    xlim(0, 20)
    ylim(0, 30)
    y = 10
    for i in range(10):
        for j in range(10):
            x = 5 + j
            plot(x, y, '-*b')
        y += 1
    show()

pointLine3()


def affine():
    xlim(0, 50)
    ylim(0, 50)
    x = 10
    y = 10
    for i in range(31):
        x = 10 + i
        y += x
        plot(x, y, '-*r')
    show()

affine()