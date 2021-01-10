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

# Genera una población de individuos aleatoriamente
def generatePopulation():
    population = []
    population = [[1,2,3,4], [1,2,4,3], [1,3,2,4]]
    
    return(population)

# Intercambia dos posiciones de una lista
def swap(list, x, y):
    temp = list[x] 
    list[x] = list[y]
    list[y] = temp

# Proceso de mutación por intercambio para un individuo seleccionado
def mutation(selectedInd):
    x = 0
    y = 0
    while x == y:
        x = random.randrange(len(selectedInd))
        y = random.randrange(len(selectedInd))
    swap(selectedInd,x,y)
    return selectedInd

# Crea una "matriz" con los pesos (distancias) entre cada vértice (ciudad)
def createWeights():
    weights = []
    weights = [[0, 7, 9, 8], [7, 0, 10, 4], [9, 10, 0, 15], [8, 4, 15, 0]]
    
    return(weights)

#Función de adaptación / evaluación
def populationEvaluation(weights, numInd, genLength, pob):
    costo= 0
    list= []
    
    for i in range(numInd):
        costo= 0
        for j in range(genLength-1):
            x= pob[i][j]
            y= pob[i][j+1]
            costo= costo + weights[x-1][y-1]
            j+=1
        primero= pob[i][0]
        ultimo= pob[i][genLength-1]
        i+=1
        list.append(costo+weights[ultimo-1][primero-1])
        
    return list

# Función para sumar las calificaciones obtenidas por cada individuo
def sumQualifications(qualifications):
    result = 0
    for q in qualifications:
        result = result + q
    return result

"""
Función de selección
    • pob: es la una lista anidada donde se encuentra todos los posibles caminos
    • weights: es la lista anidada que tiene los pesos de cada ciudad
    • numInd: es el número de individuos en la población
    • selOp: variable que define que se quiere seleccionar si el mayor o menor
"""
def selection(pob, weights, numInd, selOp):
    
    if selOp == 0:
        # Se toma el primer valor como el menor
        menor= weights[0]
        
        for i in range(numInd):
            if menor > weights[i]:
                menor= weights[i]
            i+=1
            
        for i in range(numInd):
            if menor == weights[i]:
                #se copia la lista que se encuentre en esa posición 
                sel= pob[i]
                break
            i+=1
    else:
        # Se toma el primer valor como el mayor
        mayor= weights[0]
        for i in range(numInd):
            if mayor < weights[i]:
                mayor= weights[i]
            i+=1
        
        for i in range(numInd):
            if mayor == weights[i]:
                #se copia la lista que se encuentre en esa posición 
                sel= pob[i]
                break
            i+=1
    
    return sel

#City es el número de ciudades
def corsses(sel, sel1, city):
    
    i=0
    temp=0
    #Se comprueba si el valor de city es impar o par
    if city % 2 == 0:
        pos1= random.randint(0, city)
        pos2= random.randint(0, city)
        while pos1 == pos2:
            pos1= random.randint(0, city)
            pos2= random.randint(0, city)
            
    else :
        pos1= random.randint(0, city-1)
        pos2= random.randint(0, city-1)
        while pos1 == pos2:
            pos1= random.randint(0, city-1)
            pos2= random.randint(0, city-1)
    
    #Para evitar que pos1 sea mayor a pos2
    if pos1 > pos2:
        temp= pos1
        pos1=pos2
        pos2= temp
    
    c1= sel[pos1+1:pos2]
    c2= sel1[pos1+1:pos2]
    
    j= pos1
    l= pos2-pos1
    m=0
    for j in range(l-1):
        sel[pos1+1]=c2[m]
        sel1[pos1+1]=c1[m]
        pos1+=1
        m+=1
        j+=1
    
    return[sel, sel1]

"""
Función principal del AG
    • numInd: Número de individuos de la población, en este ejemplo será de 3.
    • genLength: longitud del Genoma, tiene una longitud de 4.
    • numGenerations: número de Generaciones.
"""
def main(numInd, genLength, numGenerations):
    S = 0.0
    weights = []
    evaluation = []
    population = []
    newPopulation = [] 
    selectedPob = [] # Individuos seleccionados
    selMin = 0 # Se utiliza para que nos de el individuo con menos peso
    selMax = 1 #Se utiliza para que nos de el individuo con mayor peso
    weights = createWeights()
    population = generatePopulation()
    print("Población original")
    print(population)
    
    for i in range(numGenerations):
        evaluation = populationEvaluation(weights, numInd, genLength, population)
        print("Evaluación de la pob: ")
        print(evaluation)
        S = sumQualifications(evaluation)
        print("Calificación:",S," \n")
        print("---------------------")
        
        while len(newPopulation) < numInd:
            selectedPob.append(selection(population, weights, numInd, selMin))
            selectedPob.append(selection(population, weights, numInd, selMax))
            print("Individuos seleccionados: ")
            print(selectedPob)
            selectedPob = corsses(selectedPob[0], selectedPob[1], genLength)
            print("Cruza: ")
            print(selectedPob)
            mutation(selectedPob[0])
            mutation(selectedPob[1])
            print("Mutación")
            print(selectedPob)
            newPopulation = newPopulation + selectedPob
            selectedPob = []
        print("Nueva población:", i,"\n")
        print(newPopulation)
        population = []
        population = newPopulation
        newPopulation = []
    
    evaluation = populationEvaluation(weights, numInd, genLength, population)
    print("Evaluación final de la pob: ")
    print(evaluation)
    S = sumQualifications(evaluation)
    print("Calificación final:",S," \n")
    print("---------------------")
