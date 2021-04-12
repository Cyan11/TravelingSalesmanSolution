from class1 import greedySearch
from TSPHelper import TSPHelper
import random
from random import shuffle
import math

def FixPath(path):

    clean_c = []
    for val in path:
        if val not in clean_c:
         clean_c.append(val)
    #print ('Removed duplicates->' + str(clean_c))

    missing = [item for item in RandomSample if item not in clean_c]
    #print 'Missing values->' + str(missing)

    path = clean_c + missing
    return path

if __name__ == '__main__':   
    temp = 5000
    t = TSPHelper()  
    path = greedySearch(t, 0)
    path2 = path
    while temp > 0:
        RandomSample = list(range(t.getNodes()))
        shuffle(RandomSample)
        i = 0
        #try to find a better path
        while i==0:
                for node in path2:         
                    if random.randint(0, math.ceil(100/temp)+1) == 1:
                        path2[node] = RandomSample[node] 
                        i+= 1
                
                path2 = FixPath(path2)
                if not t.validatePath(path2):
                        i = 0

        path = FixPath(path)
        if t.scorePath(path2) < t.scorePath(path):
            print("New Attempt: " + str(t.scorePath(path2)) + ", Old Attempt: " + str(t.scorePath(path)) + " - New Path Chosen")
            path = path2
        else:
            print("New Attempt: " + str(t.scorePath(path2)) + ", Old Attempt: " + str(t.scorePath(path)) + " - Old Path Chosen")
            path2 = path
        i = 0
        temp = temp - 1


