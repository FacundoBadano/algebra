from graphics import *
import math

def main():
    win = GraphWin("Antena Fractal", 700, 900)

    dif = 66.9872981077807

    rect = Rectangle(Point(100,100 + dif), Point(350,350 + dif))
    rect.draw(win)
    rect2 = Rectangle(Point(355,100 + dif), Point(605,350 + dif))
    rect2.draw(win)

    rect3 = Rectangle(Point(351.5,100 + dif), Point(351.5,350 + dif))
    rect3.draw(win)

    altura = (((500)*math.sqrt(3))/2)
    print("Altura del triangulo:", altura)
    print(500-((((500)*math.sqrt(3))/2)))

    A = Point(100,800)
    B = Point(600,800)
    C = Point(351.5, altura)

    def getCoordenadaCorte(pointA, pointB, pointC):
        print("Coordenadas X:", pointA.getX(), pointB.getX(), pointC.getX())
        print("Coordenadas Y:", pointA.getY(), pointB.getY(), pointC.getY())

        Corte1 = operacionCoord(pointC, pointA)
        Corte2 = operacionCoord(pointC, pointB)
        Corte3 = operacionCoord(pointA, pointB)
        
        subpoli = Polygon(Corte1, Corte2, Corte3)
        subpoli.draw(win)

        return (subpoli.getPoints())


    def operacionCoord(point1, point2):
        x = (point1.getX() / 2 + point2.getX() / 2)
        y = (point1.getY() / 2 + point2.getY() / 2)
        
        return Point(x,y)

    poli = Polygon(A,B,C)
    poli.draw(win)

    mayor = getCoordenadaCorte(A,B,C)
    test = getCoordenadaCorte(mayor[0],mayor[1],C)
    tes2 = getCoordenadaCorte(mayor[0],mayor[2],A)
    tes3 = getCoordenadaCorte(mayor[1],mayor[2],B)


    # x = Polygon(Point(1,1), )
    win.setBackground("white")
    # win.getMouse() # Pause to view result

    while True:
        print(win.getMouse())


    # win.close()    # Close window when done

main()

