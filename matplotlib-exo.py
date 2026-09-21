from pylab import *

def triangle():
    xlim(0, 10)
    ylim(0, 10)
    x = [2, 5, 8]
    y = [2, 8, 2]
    plot(x, y, '*r')
    show()

triangle()