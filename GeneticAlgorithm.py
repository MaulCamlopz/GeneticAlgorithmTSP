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
            column.append(random.randint(10, 50))
        matrix.append(column)
    return(matrix)

