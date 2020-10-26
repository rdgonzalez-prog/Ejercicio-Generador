# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:41:16 2020

@author: rdgonzalezj
"""
# Esta función permite consultar al usuario un número
# en el rango (ini, fin) y devolverlo

def leer_numero (ini, fin, mensaje): 
    num = ini - 1
    while num < ini or num > fin:     
        print (mensaje) 
        num = int (input ()) 
    
    return num

# Esta función permite generar cantidad numeros aleatorios tipo float y redondearlos
# La cantidad y tipo de redondeo se obtiene a través de consola, una vez que se realiza el llamado a la función leer_numero
# Los numeros aleatorios y su redondeo son mostrados en pantalla, también se genera una lista con los numeros redondeados
def generador ():
    import random
    import math
    numeros = leer_numero(1, 20, "Cuantos numeros quiere generar? [1-20]")
    modo = leer_numero(1, 3, "Como quiere redondear los numeros? [1] Al alza [2] A la baja [3] Normal:")
    lista_aleatorios = []
    for i in range (numeros):
        lista_aleatorios.append(random.uniform (0, 100))
        auxiliar = lista_aleatorios [i]
        if modo == 1:
            lista_aleatorios [i] = math.ceil(lista_aleatorios [i])
        else:
                if modo == 2:
                    lista_aleatorios [i] = math.floor(lista_aleatorios [i])
                else:
                        lista_aleatorios [i] = round(lista_aleatorios [i])
                        
        print ('Aleatorio:', auxiliar, "Redondeado: ", lista_aleatorios[i])
        
    return lista_aleatorios
    
    
    



