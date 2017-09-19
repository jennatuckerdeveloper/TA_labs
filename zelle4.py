from graphics import *

def main():
    win = GraphWin('Click me!')
    for i in range(10):
        p = win.getMouse()
        p = p.draw(win)
        print("You clicked at:", p.getX(), p.getY())

main()

def main2():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0, 0.0 )

main2()