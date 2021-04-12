import random
import json
from copy import deepcopy


class TSPHelper(object):

    def __init__(self):
        random.seed(12312323)
        self._graph = {}
        with open('graph.json') as graph:
            g = json.load(graph)

            for k, v in g.items():
                self._graph[int(k)] = {}
                for kP, vP in v.items():
                    self._graph[int(k)][int(kP)] = int(vP)

        self._nodes = len(self._graph.keys())
        self._minPathLength = self._nodes

    def getNodes(self):
        return self._nodes

    def _generateGraph(self, n, minCost, maxCost) :
        #N nodes
        nodes = tuple(range(n))
        availNodes = list(deepcopy(nodes))
        graph = {}
        for node in nodes:
            graph[node] = {}

            del (availNodes[0])

            for destination in availNodes :
                cost = random.randint(minCost, maxCost)
                graph[node][destination] = cost

        #2nd pass
        availNodes = list(deepcopy(nodes))
        for node in nodes:
            del (availNodes[0])

            for destination in availNodes :
                cost = random.randint(minCost, maxCost)
                graph[destination][node] = cost

        return graph

    def _splitToPairs(self, path):
        return zip(path[:-1], path[1 :])

    def _costArc(self, f, t):
        return self._graph[f][t]

    def validatePath(self, path):

        #Check the length of the path
        if len(path) < self._minPathLength:
            raise Exception('Length of a valid path should be at least->' + str(self._minPathLength) + ', length of path provided->' + str(len(path)))

        #Assert no self-loops
        for fromNode, destNode in self._splitToPairs(path):
            if fromNode == destNode:
                raise Exception('Path contains a self loop: ' + str(fromNode) + '->' + str(destNode))

        #Assert all types are numeric
        if not all(isinstance(item, int) for item in path):
            raise Exception('Path contains non int types!')

        #Assert the path goes to every node
        if not set(path) == set(self._graph.keys()):
            raise Exception('Path does not reach every node!')

        return True

    def scorePath(self, path, validate = True):

        #Validate the path
        if validate:
            self.validatePath(path)

        #Split to pairs
        pairs = self._splitToPairs(path)

        #Cost
        cost = 0
        for fromNode, destNode in pairs:
            cost += self._costArc(fromNode, destNode)
        cost += self._costArc(path[-1], path[0])
        return cost

if __name__ == '__main__':
    print("a")
    from time import time
    t = TSPHelper()
    #pprint(t._graph)

    path = list(range(len(t._graph.keys())))
    print (t._costArc(0, 9) )
    print (t._costArc(9, 0) )
    print (t.validatePath(path) )
    print (t.scorePath(path) )

    nums = list(range(len(t._graph.keys())))
    minS = 99999999999
    maxS = 0
    random.seed(time())
    for _itt in range(1000):

        p = deepcopy(nums)
        random.shuffle(p)
        p = p
        score = t.scorePath(p)
        if score > maxS:
            maxS = score
        if score < minS:
            minS = score
        print ('Score->' + str(score) + ', min->' + str(minS) + ', max->' + str(maxS) )