# Se importan las funciones del archivo jobshop.py
from jobshopproblem import *

# Se importan los módulos necesarios
import math
import random
import time
import numpy
import matplotlib.pyplot as plt

# Función que genera vecinos realizando un swap de las posiciones del array
# Entrada: state        -> solución actual
#          mode         -> forma en la que se realiza el swap (secuencial o random)
# Salida:  allNeighbors -> array de vecinos (soluciones) a la solución que se ingreso como entrada
def getNeigbors(state, mode="normal"):
    allNeighbors = []

    for i in range(len(state)-1):
        neighbor = state[:]
        if mode == "normal":
            swapIndex = i + 1
        elif mode == "random":
            swapIndex = random.randrange(len(state))
        neighbor[i], neighbor[swapIndex] = neighbor[swapIndex], neighbor[i]
        allNeighbors.append(neighbor)

    return allNeighbors

# Función que implementa el algoritmo de Simmulated Annealing
# Entrada: jobs        -> array de 2 dimensiones que contiene las máquinas y los tiempos de la instancia del problema
#          T           -> Temperatura 
#          termination -> cantidad de iteraciones
#          halting     -> cantidad de veces que se disminuye la temperatura
#          mode        -> forma en la que se realiza el swap al crear los vecinos (secuencial o random)
#          decrease    -> porcentaje de disminución de la temperatura
# Salida:  actualCost  -> makespan de la solución encontrada
#          state       -> solución encontrada 
def simulatedAnnealing(jobs, T, termination, mode, decrease, printSolutions = False):
    numberOfJobs = len(jobs)
    numberOfMachines = len(jobs[0])

    execution = time.time()
    state = randomSchedule(numberOfJobs, numberOfMachines)

    solutionsCosts = [] 

    while(T > 1):
        T = decrease * float(T)

        for k in range(termination):
            actualCost = cost(jobs, state)

            for n in getNeigbors(state, mode):
                nCost = cost(jobs, n)
                if nCost < actualCost:
                    state = n
                    actualCost = nCost
                else:
                    delta = abs(nCost - actualCost)
                    probability = math.exp(-delta/T)
                    if random.random() < probability:
                        state = n
                        actualCost = nCost
                solutionsCosts.append(actualCost)
    execution = time.time() - execution
    if printSolutions == True:
        printSearch(solutionsCosts, "Búsqueda de Soluciones con SA")

    return actualCost, state, solutionsCosts, execution

def simulatedAnnealingImproved(jobs, numExperiments, T, termination, halting, mode, decrease):
    solutions = []
    best = 10000000
    solutionsCosts = []
    execution = time.time()
    for i in range(numExperiments):
        cost, schedule, solutionsCost, e = simulatedAnnealing(jobs, T=T, termination=termination, mode=mode, decrease=decrease, printSolutions=False)
        solutionsCosts = solutionsCosts + solutionsCost
        if cost < best:
            best = cost
            solutions.append((cost, schedule))
    execution = time.time() - execution      
    printSearch(solutionsCosts, "Búsqueda de Soluciones con SA improved")
    print(solutions[-1])
    return solutions[-1][0], solutions[-1][1], execution


def printSearch(solutionsCosts, title):
    x = range(len(solutionsCosts))

    plt.plot(x, solutionsCosts)
    plt.xlabel('Iteraciones')
    plt.ylabel('Makespan (Función Objetivo)')
    plt.title(title)
    plt.show()