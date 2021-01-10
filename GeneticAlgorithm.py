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
def generatePopulation(numInd, genLength):
    population = []
    #population = [[1,2,3,4], [1,2,4,3], [1,3,2,4]]
    for i in range(numInd):
        item = []
        for j in range(genLength):
            item.append(j+1)
        random.shuffle(item)
        population.append(item)
    return(population)

# Intercambia dos posiciones de una lista
def swap(list, x, y):
    temp = list[x] 
    list[x] = list[y]
    list[y] = temp

# Proceso de mutación por intercambio para un individuo seleccionado
def mutation(selectedPob, pM):
    i= 0
    q = 0.0
    while i < 2:
        q = random.random()
        if q < pM:
            x = 0
            y = 0
            print("\nMutación\n")
            print(selectedPob[i])
            while x == y:
                x = random.randrange(len(selectedPob[i]))
                y = random.randrange(len(selectedPob[i]))
            swap(selectedPob[i],x,y)
            print(selectedPob[i])
            print("\n")   
        i+=1


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
    • GENOME_LENGTH: longitud del Genoma, tiene una longitud de 4.
    • numGenerations: número de Generaciones.
    • pM: probabilidad de mutación
"""
def main(numInd, pM, numGenerations):
    S = 0.0
    GENOME_LENGTH = 4
    weights = []
    evaluation = []
    population = []
    newPopulation = [] 
    selectedPob = [] # Individuos seleccionados
    selMin = 0 # Se utiliza para que nos de el individuo con menos peso
    selMax = 1 #Se utiliza para que nos de el individuo con mayor peso
    weights = createWeights()
    population = generatePopulation(numInd, GENOME_LENGTH)
    print("Población original")
    print(population)
    
    for i in range(numGenerations):
        evaluation = populationEvaluation(weights, numInd, GENOME_LENGTH, population)
        print("Evaluación de la pob: ")
        print(evaluation)
        print("El mejor de la generación es el: ",getMinList(evaluation),"\n")
        S = sumQualifications(evaluation)
        print("Calificación:",S," \n")
        print("---------------------")
        
        while len(newPopulation) < numInd:

            selectedPob.append(selection(weights, numInd, GENOME_LENGTH, population));
            selectedPob.append(selection(weights, numInd, GENOME_LENGTH, population));
            print("Individuos seleccionados: ")
            print(selectedPob)

            selectedPob = corsses(selectedPob[0], selectedPob[1], GENOME_LENGTH)
            print("Cruza: ")
            print(selectedPob)
            
            mutation(selectedPob, pM)
            
            print("selectedPob")
            print(selectedPob)
            
            newPopulation = newPopulation + selectedPob
            selectedPob = []
        print("Nueva población:", i,"\n")
        print(newPopulation)
        population = []
        population = newPopulation
        newPopulation = []
    
    evaluation = populationEvaluation(weights, numInd, GENOME_LENGTH, population)
    print("Evaluación final de la pob: ")
    print(evaluation)
    print("El mejor de la generación es el: ",getMinList(evaluation),"\n")
    S = sumQualifications(evaluation)
    print("Calificación final:",S," \n")
    print("---------------------")
