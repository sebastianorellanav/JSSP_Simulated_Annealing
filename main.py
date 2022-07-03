from jobshopproblem import *
from simulated_annealing import *

if __name__ == '__main__':

    # Se lee el archivo y se almacenan las secuencias de las operaciones en cada máquina junto con
    # el tiempo que demora cada operación
    jobs = readFile('instancias/10x10')

    # Se imprimen los datos de la instancia escogida
    numMachines = len(jobs[0])
    numJobs = len(jobs)
    print("Instancia Escogida:", 'instancias/3x3')
    print("Cantidad de Maquinas:", numMachines)
    print("Cantidad de Trabajos:", numJobs)
    printJobs(jobs)

    # Se utiliza la metaheurística de Simulated Annealing para encontrar una solución de
    # buena calidad que se aporxime al óptimo del problema
    start_time = time.time()
    cost, solution = simulatedAnnealing(jobs,  
                                        T=int(200), 
                                        termination=int(20), 
                                        halting=int(10), 
                                        mode='random', 
                                        decrease=float(0.8))

    end_time = time.time()
    print("La solución optima encontrada es:")
    print(cost, solution)
    
    # Se imprime la solución encontrada
    #printSchedule(jobs, solution)

    # Se imprime el tiempo de ejecución
    print("La búsqueda demoró {:.1f} segundos".format(end_time - start_time))

    ############################################################################################
    start_time = time.time()
    cost, solution = simulatedAnnealingImproved(jobs,
                                                numExperiments=40,  
                                                T=int(200), 
                                                termination=int(20), 
                                                halting=int(10), 
                                                mode='random', 
                                                decrease=float(0.8))

    end_time = time.time()
    print("\n\nLa solución optima encontrada es:")
    print(cost,solution)
    print("La búsqueda mejorada demoró {:.1f} segundos".format(end_time - start_time))