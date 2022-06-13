from graphics import *
import math

def main():
    win = GraphWin("Antena Fractal", 700, 900)
    dif = 71.9872981077807

    antena_1 = Rectangle(Point(100,100 + dif), Point(350,350 + dif))
    antena_2 = Rectangle(Point(355,100 + dif), Point(605,350 + dif))
    palito = Rectangle(Point(351.5,100 + dif), Point(351.5,352 + dif))
    
    antena_1.setFill("black")
    antena_2.setFill("black")
    palito.setFill("black")
    
    antena_1.draw(win)
    antena_2.draw(win)
    palito.draw(win)

    altura = (((489)*math.sqrt(3))/2)
    print("Altura del triangulo:", altura)
    print(500-((((500)*math.sqrt(3))/2)))

    A = Point(100,800)
    B = Point(600,800)
    C = Point(353, altura)

    def getCoordenadaCorte(pointA, pointB, pointC):
        print("Coordenadas X:", pointA.getX(), pointB.getX(), pointC.getX())
        print("Coordenadas Y:", pointA.getY(), pointB.getY(), pointC.getY())

        Corte1 = operacionCoord(pointC, pointA)
        Corte2 = operacionCoord(pointC, pointB)
        Corte3 = operacionCoord(pointA, pointB)
        
        subpoli = Polygon(Corte1, Corte2, Corte3)
        subpoli.setFill("white")
        subpoli.draw(win)

        return (subpoli.getPoints())

    def operacionCoord(point1, point2):
        x = (point1.getX() / 2 + point2.getX() / 2)
        y = (point1.getY() / 2 + point2.getY() / 2)
        
        return Point(x,y)

    poli = Polygon(A,B,C)
    poli.setFill("black")
    poli.draw(win)

    mayor = getCoordenadaCorte(A,B,C)
    test = getCoordenadaCorte(mayor[0],mayor[1],C)
    tes2 = getCoordenadaCorte(mayor[0],mayor[2],A)
    tes3 = getCoordenadaCorte(mayor[1],mayor[2],B)

    win.setBackground("white")

    while True:
        print(win.getMouse())


main()

