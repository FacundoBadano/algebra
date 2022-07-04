from graphics import *
import math

def main():
    win = GraphWin("Antena Fractal", 700, 900)
    win.setBackground("white")
    dif = 71.9872981077807 # Diferencia en coordenadas Y para obtener triangulo conextado a palito

    # Figuras estáticas
    antena_1 = Rectangle(Point(80,100 + dif), Point(330,350 + dif))
    antena_2 = Rectangle(Point(370,100 + dif), Point(620,350 + dif))
    palito = Rectangle(Point(339.5,100 + dif), Point(360,352 + dif))
    
    antena_1.setFill("black")
    antena_2.setFill("black")
    palito.setFill("black")
    
    antena_1.draw(win)
    antena_2.draw(win)
    palito.draw(win)

    altura = (((489)*math.sqrt(3))/2) # Calculo de la altura del triangulo

    # Coordenadas Triangulo inicial
    A = Point(100,800)
    B = Point(600,800)
    C = Point(350, altura)

    # Operación para obtener sub_triangulos a partir de coordenadas dadas por parametro
    def getSubTriangulos(pointA, pointB, pointC):
        triangulos_procesar = []
        
        CA = operacionCoord(pointC, pointA)
        BC = operacionCoord(pointB, pointC)
        AB = operacionCoord(pointA, pointB)

        sub_triangle_1 = Polygon(pointA, CA, AB)
        sub_triangle_2 = Polygon(pointB, AB, BC)
        sub_triangle_3 = Polygon(pointC, CA, BC)

        triangulos_procesar.append(sub_triangle_3)
        triangulos_procesar.append(sub_triangle_1)
        triangulos_procesar.append(sub_triangle_2)

        return triangulos_procesar

    # Operación para obtener puntos medios dados 2 puntos
    def operacionCoord(point1, point2):
        x = (point1.getX() / 2 + point2.getX() / 2)
        y = (point1.getY() / 2 + point2.getY() / 2)
        return Point(x,y)

    # Dibujado de triangulos
    def procesar_triangulos(a_procesar):
        for triangle in a_procesar:
            triangle.setFill("black")
            triangle.draw(win)
    
    # Validación para el input generador
    def check():
        resp = input("Iteracion Triangulo Sierpinski: ")
        if (resp.isnumeric() == False):
            print("Error. No se recibio numero. Intente nuevamente")
            check()
        else:
            if(int(resp)<1):
                print("Error. No se recibio numero positivo. Intente nuevamente")
                check()
            else:
                sierpinski(esfuerzo(resp))    

    # Cantidad de triangulos a procesar
    def esfuerzo(resp):
        suma = 0
        for n in range(int(resp)):
            suma += (3 ** n)

        print("Esfuerzo:", suma)
        return suma

    # Armado del triangulo a partir de esfuerzo indicado
    def sierpinski(obj):
        triangulo_mayor = Polygon(A,B,C)
        aux_triangulos = [triangulo_mayor]
        objetivo = obj

        for x in range (objetivo):
            vert_data = aux_triangulos.pop(0).getPoints()
            generados = getSubTriangulos(vert_data[0], vert_data[1], vert_data[2])
            for triangulo in generados:
                aux_triangulos.append(triangulo)
        procesar_triangulos(aux_triangulos)

        input("Antena representada con exito!\nPresiona la tecla enter para salir.")
        quit()

    check()
    

    while True:
        print(win.getMouse())

main()

