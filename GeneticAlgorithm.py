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

# Genera una población al azar
def generatePopulation(nInd, longGenoma):
    population = []
    for i in range(nInd):
        item = []
        for j in range(longGenoma):
            item.append(j+1)
        random.shuffle(item)
        population.append(item)
    return(population)

# Intercambia las posiciones de un arreglo
def swap(array, x, y):
    temp = array[x] 
    array[x] = array[y]
    array[y] = temp

# Proceso de mutación por intercambio
def mutation(array):
    x = 0
    y = 0
    while x == y:
        x = random.randrange(len(array))
        y = random.randrange(len(array))
    swap(array,x,y)
    return array

# Crea la matriz con los pesos
def createMatrix(rows, columns):
    matrix = []
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
def costRow(matrix, Nind, columns, pob):
    costo= 0
    list= []
    i=0
    j=0
    
    for i in range(Nind):
        costo= 0
        for j in range(columns-1):
            x= pob[i][j]
            y= pob[i][j+1]
            costo= costo + matrix[x-1][y-1]
            j+=1
        primero= pob[i][0]
        ultimo= pob[i][columns-1]
        i+=1
        list.append(costo+matrix[ultimo-1][primero-1])
        
    return list


def selectionFunction(pob,list, Nindi):
    
    i=0
    pos=0
    menor= list[0]
    
    for i in range(Nindi):
        if menor > list[i]:
            menor= list[i]
        i+=1
    for i in range(Nindi):
        if menor == list[i]:
           break
        i+=1
    
    return pob[i]
