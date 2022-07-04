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

    

    def getSubTriangulos(pointA, pointB, pointC):
        triangulos_procesar = []
        
        CA = operacionCoord(pointC, pointA)
        BC = operacionCoord(pointB, pointC)
        AB = operacionCoord(pointA, pointB)

        sub_triangle_1 = Polygon(pointA, CA, AB)
        sub_triangle_2 = Polygon(pointB, AB, BC)
        sub_triangle_3 = Polygon(pointC, CA, BC)

        triangulos_procesar.append(sub_triangle_1)
        triangulos_procesar.append(sub_triangle_2)
        triangulos_procesar.append(sub_triangle_3)

        return triangulos_procesar

    def operacionCoord(point1, point2):
        x = (point1.getX() / 2 + point2.getX() / 2)
        y = (point1.getY() / 2 + point2.getY() / 2)
        return Point(x,y)

    def procesar_triangulos(a_procesar):

        for triangle in a_procesar:
            triangle.setFill("black")
            triangle.draw(win)
        
    def esfuerzo():
        resp = input("Iteracion Triangulo Sierpinski: ")
        suma = 0
        for n in range(int(resp)):
            suma += (3 ** n)

        return suma

    def sierpinski():
        triangulo_mayor = Polygon(A,B,C)
        aux_triangulos = [triangulo_mayor]
        objetivo = esfuerzo()

        for x in range (objetivo):
            vert_data = aux_triangulos.pop(0).getPoints()
            generados = getSubTriangulos(vert_data[0], vert_data[1], vert_data[2])
            for triangulo in generados:
                aux_triangulos.append(triangulo)
        procesar_triangulos(aux_triangulos)

    sierpinski()
    win.setBackground("white")

    while True:
        print(win.getMouse())

main()

