# Se importan las funciones del archivo jobshop.py
from jobshopproblem import *

# Se importan los módulos necesarios
import math
import random
import time

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
def simulatedAnnealing(jobs, T, termination, halting, mode, decrease):
    numberOfJobs = len(jobs)
    numberOfMachines = len(jobs[0])

    state = randomSchedule(numberOfJobs, numberOfMachines)

    for i in range(halting):
        T = decrease * float(T)

        for k in range(termination):
            actualCost = cost(jobs, state)

            for n in getNeigbors(state, mode):
                nCost = cost(jobs, n)
                if nCost < actualCost:
                    state = n
                    actualCost = nCost
                else:
                    probability = math.exp(-nCost/T)
                    if random.random() < probability:
                        state = n
                        actualCost = nCost

    return actualCost, state

def simulatedAnnealingImproved(jobs, numExperiments, T, termination, halting, mode, decrease):
    solutions = []
    best = 10000000

    for i in range(numExperiments):
        cost, schedule = simulatedAnnealing(jobs, T=T, termination=termination, halting=halting, mode=mode, decrease=decrease)

        if cost < best:
            best = cost
            solutions.append((cost, schedule))
    
    return solutions[-1]