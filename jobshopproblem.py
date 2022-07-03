import fileinput
import random

def readFile(path=None):
    with fileinput.input(files=path) as f:
        next(f)
        jobs = [[(int(machine), int(time)) for machine, time in zip(*[iter(line.split())]*2)]
                    for line in f if line.strip()]
    return jobs

def printJobs(jobs):
    print(len(jobs), len(jobs[0]))
    for job in jobs:
        for machine, time in job:
            print(machine, time, end=" ")
        print()


def cost(jobs, schedule):
    j = len(jobs)
    m = len(jobs[0])

    tj = [0]*j
    tm = [0]*m

    ij = [0]*j

    for i in schedule:
        machine, time = jobs[i][ij[i]]
        ij[i] += 1

        start = max(tj[i], tm[machine])
        end = start + time
        tj[i] = end
        tm[machine] = end

    return max(tm)

class OutOfTime(Exception):
    pass

# Coloca todos los numeros de los jobs m veces (cantidad de maquinas)
def randomSchedule(j, m):
    schedule = [i for i in list(range(j)) for _ in range(m)]
    random.shuffle(schedule)
    return schedule



def printSchedule(jobs, schedule):
    def format_job(time, jobnr):
        if time == 1:
            return '#'
        if time == 2:
            return '[]'

        js = str(jobnr)

        if 2 + len(js) <= time:
            return ('[{:^' + str(time - 2) + '}]').format(jobnr)

        return '#' * time

    j = len(jobs)
    m = len(jobs[0])

    tj = [0]*j
    tm = [0]*m

    ij = [0]*j

    output = [""] * m

    for i in schedule:
        machine, time = jobs[i][ij[i]]
        ij[i] += 1
        start = max(tj[i], tm[machine])
        space = start - tm[machine]
        end = start + time
        tj[i] = end
        tm[machine] = end

        output[machine] += ' ' * space + format_job(time, i)

    print("")
    print("Optimal Schedule: ")
    [print("Machine ", idx, ":", machine_schedule) for idx, machine_schedule in enumerate(output)]
    print("")
    print("Optimal Schedule Length: ", max(tm))
