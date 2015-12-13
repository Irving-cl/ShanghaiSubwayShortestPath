
# Imports #
from Interface import *
import string
import Queue

# ========================================
# Class: Vertex
#   This class represents a vertex in the
# graph which stores the information of
# one station. It's basic data structure
# of this application. It has a name and a
# list of adjacent vertices.
# ========================================

class Vertex:

    #. Constructor .#
    def __init__ (self, name):
        self.name = name             # Construct with the name of the station
        self.adjVertices = []        # Initialize its adjacent vertices as empty
        self.visited = False         # To show if the vertex is visited when the algorithm is running
        self.distance = 0            # To Store the current distance from start
        self.path = None             # To Store last vertex in the path

    #. Add adjacent vertice .#
    def addAdjVertex(self, adjVertex):
        if not self.containsAdj(adjVertex):
            self.adjVertices.append(adjVertex)

    #. Get methods .#
    def getName(self):
        return self.name
    def getVisited(self):
        return self.visited
    def getPath(self):
        return self.path
    def getDistance(self):
        return self.distance
    
    #. Set methods .#
    def setVisited(self, visited):
        self.visited = visited
    def setPath(self, path):
        self.path = path
    def setDistance(self, distance):
        self.distance = distance

    #. If has already contains the adj vertex .#
    def containsAdj(self, vertex):
        for v in self.adjVertices:
            if v.name == vertex.name:
                return True
        return False

# ========================================
# Class: Graph
#   A Graph consists of many vertices. It
# has a bfs(breadth first search)method.
# After running bfs on a vertex, we can
# easily find the shortest path between
# two vertices
# ========================================

class Graph:
    
    #. Constructor .#
    def __init__ (self):
        self.vertices = []    # Initialize the vertices as emtpy list
        
    #. Read graph info from file and form the graph .#   
    def formGraph(self):
        f = open(graphInfoFile, 'r')           # Open the file of Shanghai subway info
        fileLines = f.readlines()              # Read all lines from file
        for line in fileLines:
            line = line.encode('gbk')
        numSubwayLines = int(fileLines[0])     # Number of subway lines
        existedStations = []                   # To avoid repeat stations
        # Read every subway line
        for i in range(numSubwayLines):        
            curSubwayLine = fileLines[i+1]
            stationList = string.split(curSubwayLine)
            isCircle = int(stationList[0])     # First element is 0 or 1 to show if the subway line is a circle
            if isCircle == 0:
                stationList.remove('0')
            else:
                stationList.remove('1')
            curLineVertices = []
            for station in stationList:
                if station not in existedStations:
                    curLineVertices.append(Vertex(station))
                    existedStations.append(station)
                else:
                    curLineVertices.append(self.findVertex(station))
            # Add adjcent vertices
            numVertices = len(curLineVertices)
            for j in range(1, numVertices-1):
                curLineVertices[j].addAdjVertex(curLineVertices[j-1])
                curLineVertices[j].addAdjVertex(curLineVertices[j+1])
            curLineVertices[0].addAdjVertex(curLineVertices[1])
            curLineVertices[numVertices-1].addAdjVertex(curLineVertices[numVertices-2])
            if isCircle == 1:
                curLineVertices[0].addAdjVertex(curLineVertices[numVertices-1])
                curLineVertices[numVertices-1].addAdjVertex(curLineVertices[0])
            # Merge vertices
            self.vertices = self.vertices + curLineVertices
        f.close()

    #. Find a vertex by name .#
    def findVertex(self, name):
        for v in self.vertices:
            if v.name == name:
                return v
    
    #. Clear attributes of all vertices .#
    def clearVertices(self):
        for v in self.vertices:
            v.visited = False
            v.distance = 0
            v.path = None
            
    #. Breath First Search .#
    def BFS(self, origin):
        self.clearVertices()
        queue = Queue.Queue(maxsize=-1)
        origin.visited = True
        queue.put(origin)
        while not queue.empty():
            v = queue.get()
            for adj in v.adjVertices:
                if not adj.visited:
                    adj.visited = True
                    adj.distance = v.distance + 1
                    adj.path = v
                    queue.put(adj)

    #. Return shortest path .#
    def shortestPath(self, dest):
        stack = Queue.LifoQueue(maxsize=-1)
        path = ''
        while True:
            stack.put(dest.name)
            if dest.path == None:
                break
            else:
                dest = dest.path
        while True:
            path = path + stack.get()
            if not stack.empty():
                path = path + '->'
            else:
                break
        return path

    #. Debug method .#
    def a(self):
        for v in self.vertices:
            line = v.name
            for w in v.adjVertices:
                line = line + ' ' + w.name
            print line
