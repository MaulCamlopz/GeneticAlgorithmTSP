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
def generatePopulation(numInd, Genlength):
    population = []
    for i in range(numInd):
        item = []
        for j in range(Genlength):
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
def mutation(selectedInd):
    x = 0
    y = 0
    while x == y:
        x = random.randrange(len(selectedInd))
        y = random.randrange(len(selectedInd))
    swap(selectedInd,x,y)
    return selectedInd

# Crea una "matriz" con los pesos (distancias) entre cada vértice (ciudad)
def createWeights(numInd):
    weights = []
    for i in range(numInd):
        values = [] # lista de valores por cada individuo
        for j in range(numInd):
            if i != j:
                values.append(random.randint(1, 100))
            else:
                values.append(0) # El peso es cero cuando nos referimos a la misma ciudad
        weights.append(values)
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

def crossover(sel, sel1, city):
    # city genera un error cuando es un numero impar
    i=0
    pos1= random.randint(0, city/2)
    #Se imprime solo para comprobar el valor
    print(pos1)
    pos2= random.randint(city/2, city-1)
    print(pos2)
    if pos1 == pos2:
        pos1= random.randint(0, (city/2 - 1))
        print(pos1)
        pos2= random.randint(city/2 + 1, city-1)
        print(pos2)
    
    c1= sel[pos1+1:pos2]
    c2= sel1[pos1+1:pos2]
    #comprobar que numeros se van a copiar
    print(c1)
    print(c2)
    
    j= pos1
    l= pos2-pos1
    m=0
    for j in range(l-1):
        print(pos1)
        sel[pos1]=c2[m]
        sel1[pos1]=c1[m]
        pos1+=1
        m+=1
        j+=1
    
    return[sel, sel1]

"""
Función principal del AG
    • numInd: Número de individuos de la población.
    • genLength: longitud del Genoma.
    • numGenerations: número de Generaciones.
"""
def main(numInd, genLength, numGenerations):
    S = 0.0
    weights = []
    evaluation = []
    population = []
    newPopulation = [] 
    selectedPob = [] # Individuos seleccionados
    selOp = 0 # Se toma el primer valor como el menor
    weights = createWeights(genLength)
    population = generatePopulation(numInd, genLength)
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
            selectedPob.append(selection(population, weights, numInd, selOp))
            selectedPob.append(selection(population, weights, numInd, selOp))
            print("Individuos seleccionados: ")
            print(selectedPob)
            selectedPob = crossover(selectedPob[0], selectedPob[1], genLength)
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
