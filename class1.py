from time import time
from TSPHelper import TSPHelper
import random
import json
from copy import deepcopy

def  greedySearch(t, n):
    node = n
    path = []
    path.append(n)
    while len(path) != len(t._graph.keys()):
        currentCost = float("inf")
        currentNode = None
        for nodePrime in range(len(t._graph.keys())):
            if node != nodePrime and nodePrime not in path:
                cost = t._costArc(node, nodePrime)
                if currentCost > cost:
                    currentCost = cost
                    currentNode = nodePrime
                    
        path.append(currentNode)
        #print(str(path))
        print( 'Node' + str(node) + '->' + str(currentNode) + ', cost->' + str(currentCost))
        node = currentNode
    print(t.validatePath(path))
    print(t.scorePath(path))
    return path

#Based on the average distance to all other unexplpored nodes 
def H1(n, t, path):
    h = 0
    i = 0
    for nodePrime in t._graph.keys():
        if nodePrime not in path and n != nodePrime:
            h += t._costArc(n , nodePrime)  
            i += 1
    return h/i

#Same thing but only considers a percent of all nodes to make it quicker
def QuickH1(n, t, path, _percent):
    percent = _percent/100
    h = 0
    i = 0
    for nodePrime in t._graph.keys():
        if nodePrime not in path and n != nodePrime and i<len(t._graph.keys())*percent:
            h += t._costArc(n , nodePrime)  
            i += 1
    return h/i

#Based on the shortest connection a given node has (essentially amounts to a depth-2 greedy search)
def H2(n, t, path):
    currentCost = float("inf")
    for nodePrime in t._graph.keys():
        if nodePrime not in path and n != nodePrime:
                cost = t._costArc(n, nodePrime)
                if currentCost > cost:
                    currentCost = cost
    return currentCost   

#Same thing but only considers a percent of all nodes to make it quicker
def QuickH2(n, t, path, _percent):
    percent = _percent/100
    currentCost = float("inf")
    i = 0
    for nodePrime in t._graph.keys():
        i += 1
        if nodePrime not in path and n != nodePrime and i<len(t._graph.keys())*percent:
                cost = t._costArc(n, nodePrime)
                if currentCost > cost:
                    currentCost = cost
    return currentCost     

#Based on the average distance all other nodes have to this one 
def H3(n, t, path):
    h = 0
    i = 0
    for nodePrime in t._graph.keys():
        if nodePrime not in path and n != nodePrime:
            h += t._costArc(nodePrime , n)  
            i += 1
    return h/i

#Same thing but only considers a percent of all nodes to make it quicker
def QuickH3(n, t, path, _percent):
    percent = _percent/100
    h = 0
    i = 0
    for nodePrime in t._graph.keys():
        if nodePrime not in path and n != nodePrime and i<len(t._graph.keys())*percent:
            h += t._costArc(nodePrime , n)  
            i += 1
    return h/i

def H4(t, cutoff):
    h = {}
    for node in t._graph.keys():
        cost = []
        for nodePrime in t._graph.keys():
            if node != nodePrime:
                cost.append(t._costArc(node,nodePrime))
        cost = sorted(cost)
        cost = cost[: int( len(cost) * cutoff )]
        h[node] = float( sum(cost)) / float( len(cost))

    return h

def  AStar(t, n):
    h = H4(t, 0.01)
    node = n
    path = []
    path.append(n)
    while len(path) != len(t._graph.keys()):
        currentCost = float("inf")
        currentNode = None
        for nodePrime in range(len(t._graph.keys())):
            #h = QuickH1(nodePrime, t, path, 5)
            if node != nodePrime and nodePrime not in path:
                cost = t._costArc(node, nodePrime) + h[nodePrime]
                if currentCost > cost:
                    currentCost = cost
                    currentNode = nodePrime
                    
        path.append(currentNode)
        #print(str(path))
        print( 'Node' + str(node) + '->' + str(currentNode) + ', Cost->' + str(currentCost - h[currentNode]) + ', Heuristic->' +str(h[currentNode]))
        node = currentNode
    print(t.validatePath(path))
    print(t.scorePath(path))
    return path
if __name__ == '__main__':
    #print("a")
    t = TSPHelper()
    #path = []
    #i = 2
    #while i < 1000:
    #    i = i + 1
    #    path.append(i)
    #H(1, t, path )
    scores = []
    score2 = "ab"
    for nodePrime in range(len(t._graph.keys())):
        score = t.scorePath(greedySearch(t, nodePrime))
        a1 = str(score)[0]
        a2 = str(score)[1]
        score2 = a1 + a2
        if score2 not in scores:
            scores.append(score2)
            print(score2)
        score2 = "ab"
    #AStar(t, 0)
    #pprint(t._graph)

    #path = list(range(len(t._graph.keys())))
    #print (t._costArc(0, 9) )
    #print (t._costArc(9, 0) )
    #print (t.validatePath(path) )
    #print (t.scorePath(path) )

    
       

   
            



    #nums = list(range(len(t._graph.keys())))
    #minS = 99999999999
    #maxS = 0
    #random.seed(time())
    #for _itt in range(1000):

       # p = deepcopy(nums)
       # random.shuffle(p)
       # p = p
       # score = t.scorePath(p)
       # if score > maxS:
        #    maxS = score
      #  if score < minS:
       #     minS = score
      #  print ('Score->' + str(score) + ', min->' + str(minS) + ', max->' + str(maxS) )




