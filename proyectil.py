import math
from sympy import symbols, Eq, solve

#Le pido al usuario que me proporcionelos distintos valores iniciales asumiendo que la x inicial es igual a 0
altura_inicial = float(input("Altura inicial del proyectil / Posición inicial del proyectil en el eje y (en metros): "))
angulo_de_trayectoria = float(input("Ángulo con respecto a la horizontal con el que se lanza el proyectil (en grados): "))
velocidad_inicial = float(input("Velocidad inicial del proyectil (en metros/segundos): "))

#Convierto a radianes el angulo 
angulo = math.radians(angulo_de_trayectoria)

#Calculo la velocidad inicial en los distintos ejes
velocidad_eje_X = velocidad_inicial * math.cos(angulo)
velocidad_eje_Y = velocidad_inicial * math.sin(angulo)

#Definto tanto t (tiempo) como x (posición)
t = symbols('t')
x = symbols('x')

#Escribo la ecuación del movimiento rectilíneo uniformemente acelerado que se da en el eje y
ecuacion_posicion_y = Eq(-4.9 * t**2 + velocidad_eje_Y * t + altura_inicial, 0)

#Resuelvo la ecuación para hallar los valores de t en los que y coincide con la horizontal
tiempo_de_vuelo = solve(ecuacion_posicion_y, t)

#Escojo el valor de t que me es util y manejo los posibles errores
if tiempo_de_vuelo:
    tiempo_de_vuelo = tiempo_de_vuelo[1].evalf()

    #Defino la ecuación del movimiento rectilineo uniforme que se da en el eje x
    ecuacion_posicion_x = Eq(velocidad_eje_X * tiempo_de_vuelo, x)

    #Resuelvo la ecuación para allar la posición donde ha caído el proyectil
    posicion_final_x = solve(ecuacion_posicion_x, x)[0].evalf()
    #Escribo el resultado
    print("El proyectil ha caído a",posicion_final_x,"metros transcurridos",tiempo_de_vuelo," segundos.")
else:
    print("El proyectil no toca el suelo. Verifica tus entradas.")