import random
from TSPHelper import TSPHelper
from random import shuffle
from class1 import greedySearch

if __name__ == '__main__':

    #Variables
    populationSize = 25
    generations = 100
    selectionRatio  = 0.25

    #Initial helper class
    t = TSPHelper()    

    #print(t.getNodes())

    #Generating random population
    population = []
    for itt in range(populationSize) :
       # path = list(range(t.getNodes()))
        #shuffle(path)
        path = greedySearch(t, itt)
        print (str(t.validatePath(path)) + ', ' + str(t.scorePath(path)) + ', ' + str(path))

        population.append(path)

    newPopulation = []
    bestPathScore = None
    bestPath = None
    lastScore = None
    currentGen = 0
    lastUpdatedGen = 0
    cumlSum = 0
    for generation in range(generations):
        currentGen += 1

        while len(newPopulation) != populationSize:

            scoredPopulation = [(t.scorePath(v), v) for v in population]
            scoredPopulation = sorted(scoredPopulation, key = lambda i: i[0])

            a = scoredPopulation[random.randint(0, int(selectionRatio * (populationSize - 1)))][1]
            b = scoredPopulation[random.randint(0, int(selectionRatio * (populationSize - 1)))][1]
            i = 0
            

            
            #print 'a->' + str(a)
            #print 'b->' + str(b)

            split = random.randint(0, len(a))
            #print 'Split is->' + str(split)

            c = a[:split] + b[split:]
            #print 'Dirty crossover->' + str(c)

            clean_c = []

            for val in c:
                if val not in clean_c:
                    clean_c.append(val)
            #print 'Removed duplicates->' + str(clean_c)

            missing = [item for item in b if item not in clean_c]
            #print 'Missing values->' + str(missing)

            c = clean_c + missing
            #print 'Final crossover->' + str(c)

            newPopulation.append(c)

        #End of a generation
        cumlSum = 0
        for path in newPopulation:
            score = t.scorePath(path)

            if bestPathScore is None or score < bestPathScore:
                bestPathScore = score
                bestPath = path

            cumlSum += score

        print ('Generation->' + str(generation)  + ', average score for generation->' + str(cumlSum / populationSize) + ', best score->' + str(bestPathScore)  )
        if selectionRatio == 0.99 :
            selectionRatio = 0.30
       
        if lastScore == cumlSum/ populationSize and 1 < currentGen - lastUpdatedGen:
            selectionRatio = 0.99
            lastUpdatedGen = currentGen
       
        lastScore = cumlSum / populationSize
        population = newPopulation
        newPopulation = []



