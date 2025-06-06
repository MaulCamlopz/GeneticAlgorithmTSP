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
import copy

# Genera una población de individuos aleatoriamente
def generatePopulation(numInd, genLength):
    population = []
    #population = [[1,2,3,4], [1,2,4,3], [1,3,2,4]]
    for i in range(numInd):
        item = []
        for j in range(genLength):
            item.append(j+1)
        random.shuffle(item)
        population.append(item)
    return population

# Intercambia dos posiciones de una lista
def swap(list, x, y):
    temp = list[x] 
    list[x] = list[y]
    list[y] = temp

# Proceso de mutación por intercambio para un individuo seleccionado
def mutation(sel, pM):
    l = copy.copy(sel)
    q = 0.0
    q = random.random()
    if q < pM:
        x = 0
        y = 0
        print("mutation")
        print(l)
        while x == y:
            x = random.randrange(len(l))
            y = random.randrange(len(l))
        swap(l,x,y)
        print(l)
    return l

# Crea una "matriz" con los pesos (distancias) entre cada vértice (ciudad)
def createWeights():
    weights = [[0, 7, 9, 8], [7, 0, 10, 4], [9, 10, 0, 15], [8, 4, 15, 0]]
    return weights

#Función de adaptación / evaluación
def populationEvaluation(weights, numInd, genLength, pob):
    list = []
    for i in range(numInd):
        costo = 0
        for j in range(genLength-1):
            x = pob[i][j]
            y = pob[i][j+1]
            costo = costo + weights[x-1][y-1]
        primero = pob[i][0]
        ultimo = pob[i][genLength-1]
        costo = costo + weights[ultimo-1][primero-1]
        list.append(costo)
        
    return list

# Función para sumar las calificaciones obtenidas por cada individuo
def sumQualifications(qualifications):
    result = 0
    for q in qualifications:
        result = result + q
    return result

def getMinList(list):
    minList = 0
    value = list[0]
    for i in range(len(list)):
        if list[i] < value:
            value = list[i]
            minList = i
    return minList

"""
Función de selección por torneo
    • pob: es la una lista anidada donde se encuentra todos los posibles caminos
    • weights: es la lista anidada que tiene los pesos de cada ciudad
    • genLength: es el número de longitud del genoma (4)
    • selOp: variable que define que se quiere seleccionar si el mayor o menor
"""
def selection(weights, numInd, genLength, pob):
    random.shuffle(pob)
    e = populationEvaluation(weights, numInd, genLength, pob)
    value = e[0]
    minList = 0
    r = random.randint(2, 3)
    for i in range(r):
        if e[i] < value:
            value = e[i]
            minList = i
    return pob[minList]

#City es el número de ciudades
def corsses(sel, sel1, city):
    
    sl= copy.copy(sel)
    sl1= copy.copy(sel1)
    i=0
    j=0
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
    
    c1= sl[pos1+1:pos2]
    c2= sl1[pos1+1:pos2]
    
    tam= len(sl1)
    tam1= len(sl)
    cpy=1
    ps=pos1 #para poder utilizarlo dentro del for
    
    for j in range(len(c1)):
        for i in range(tam):
            if c1[j] == sl1[i]:
                cpy=0
            i+=1
        if cpy == 1:
            ps+=1
            sel1[ps]= c1[j]
        j+=1
    
    ps=pos1
    for j in range(len(c2)):
        for i in range(tam1):
            if c2[j] == sl[i]:
                cpy=0
            i+=1
        if cpy == 1:
            ps+=1
            sl1[ps]= c2[j]
        j+=1
    
    return [sl, sl1]

"""
Función principal del AG
    • numInd: Número de individuos de la población, en este ejemplo será igual o mayor a 3.
    • GENOME_LENGTH: longitud del Genoma, tiene una longitud de 4.
    • numGenerations: número de Generaciones.
    • pM: probabilidad de mutación
"""
def main(numInd, pM, numGenerations):
    S = 0.0
    GENOME_LENGTH = 4
    weights = []
    population = []
    evaluation = []
    
    weights = createWeights()
    population = generatePopulation(numInd, GENOME_LENGTH)
    print("Población original")
    print(population)
    
    for i in range(numGenerations):
        newPopulation = []
        evaluation = populationEvaluation(weights, numInd, GENOME_LENGTH, population)
        print("Evaluación de la pob: ")
        print(evaluation)
        print("El mejor de la generación es el: ",getMinList(evaluation),"\n")
        S = sumQualifications(evaluation)
        print("Calificación:",S," \n")
        print("---------------------")

        while (len(newPopulation) < numInd):
            print("init selectedPob")
            print(population)
            selectedPob = []

            selectedPob.append(selection(weights, numInd, GENOME_LENGTH, population))
            selectedPob.append(selection(weights, numInd, GENOME_LENGTH, population))

            print("Individuos seleccionados: ")
            print(selectedPob)


            selectedPob = corsses(selectedPob.pop(), selectedPob.pop(), GENOME_LENGTH)
            print("Cruza: ")    
            print(selectedPob)

            selectedPob.append(mutation(selectedPob.pop(), pM)) 
            selectedPob.append(mutation(selectedPob.pop(), pM))

            print("finalSelectedPob")
            print(selectedPob)

            newPopulation = newPopulation + selectedPob
            
        
        print("---------------------")
        print("Nueva población:", i,"\n")
        print(newPopulation)
        population = newPopulation
    
    evaluation = populationEvaluation(weights, numInd, GENOME_LENGTH, population)
    print("Evaluación final de la pob: ")
    print(evaluation)
    print("El mejor de la generación es el: ",getMinList(evaluation),"\n")
    S = sumQualifications(evaluation)
    print("Calificación final:",S," \n")
    print("---------------------")
