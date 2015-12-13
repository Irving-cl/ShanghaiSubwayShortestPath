
# Imports #
from Interface import *
from Graph import *

# ========================================
# Class: Application
#   To run the application, we just create
# a instance of this class. It has two 
# main member: interface for interacting
# with users and graph for finding
# shortest path. This class let its two
# members interact.
# ========================================

class Application:

    #. Contructor .#
    def __init__ (self):
        self.interface = Interface(self.ButtonCallBack)    # Create an interface
        self.graph = Graph()                               # Create a graph
        self.graph.formGraph()                             # Form the graph
        
    #. Call back function when button is pressed .#
    def ButtonCallBack(self):
        startName = self.interface.getStartEntry().encode('gbk')
        destName = self.interface.getDestEntry().encode('gbk')
        start = self.graph.findVertex(startName)           # Find the start vertex
        dest = self.graph.findVertex(destName)             # Find the dest vertex
        # If start or dest are not found
        if start == None:
            result = startName.encode('utf8') + ' doesn\'t exist'
        elif dest == None:
            result = destName.encode('utf8') + ' doesn\'t exist'
        else:    # Normal case
            self.graph.BFS(start)
            result = self.graph.shortestPath(dest).encode('utf8')
        self.interface.updateText(result)

    #. Run the program .#
    def run(self):
        mainloop()
