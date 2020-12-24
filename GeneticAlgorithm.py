#
#  GeneticAlgorithm.py
#  Tarea XI: Aplicación de los Algoritmos Genéticos en problemas de búsqueda NP
#
#  Created by Camacho López Raúl Josafath.
#  Created by García Alonso Giovanni.
#  Copyright © 22/12/2020 UACM. All rights reserved.
#
import math
import random

def createMatrix(rows, columns):
    matrix = []
    poblacion = []
    for i in range(rows):
        column = []
        for j in range(columns):
            #Se modifico esta parte para que cuando sean entre ellos mismos sean cero ya que no hay
            # una arista entre si misma
            if i != j:
                column.append(random.randint(10, 50))
            else:
                column.append(0)
        matrix.append(column)
    return(matrix)

#Función de adaptacion
#se corrigio la función ya esta probada y funciona
def costoFila(arr, rows, columns):
    costo= 0
    fila= []
    i=0
    j=0
    
    for i in range(rows-1):
        costo= 0
        for j in range(columns-1):
            costo= costo + arr[i][j]
            j+=1
            print(costo)
        i+=1
        fila.append(costo+arr[0][columns-1])
        
    return fila

def funcionSeleccion(arr,fila, rows):
    
    i=0
    sel= []
    pos=0
    menor= fila[0]
    
    for i in range(rows-1):
        if menor > fila[i]:
            menor= fila[i]
        i+=1
    for i in range(rows-1):
        if menor == fila[i]:
           sel.append(arr[i])
        i+=1
    
    
    return(sel)
