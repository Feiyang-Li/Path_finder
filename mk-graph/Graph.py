## Must first consider what is a Graph.
# Graph is created by the connection of nodes.
# The purpose of graph is to later find a fast algorithm that get me from A to B

class GraphicalError(Exception):
    pass

class GraphicalErrorExistenceAdding(GraphicalError):
    pass

class GraphicalErrorNoExistance(GraphicalError):
    pass


class node:
    def __init__(self, name, value_store):
        self.name = name
        self.value = value_store
    

    def __str__(self):
        return self.name
    

    def __delete__(self):
        del self.value


class Graph:
    def __init__(self):
        #  node hold the value of node
        self.nodes = {}
        #  edges hold the connection of the nodes with weight
        self.edges = {}
    
    def add_nodes(self, name, value = None):
        """
        Initialize the node into the graph, it must be called before adding connection.
        name = the name of the key
        value = the value that the node hold
        """
        ## check if name exist:
        if name in self.nodes:
            raise GraphicalErrorExistenceAdding()
        else:
            print("Added node: {}".format(name))
            self.nodes[name] = value
        
    def change_node(self, name, value):
        """
        Change the value of node with name to value
        name = the name of the key
        value = the value that the node hold
        """
        if name not in self.nodes:
            raise GraphicalErrorNoExistance
        else:
            print("Changed node: {}".format(name))
            self.nodes[name] = value

    def add_path(self, name1, name2, weight = 1):
        """
        Add an road between name1 and name2
        name1 = name of node 1
        name2 = name of node 2
        weight = weight of path between
        """
        if name1 not in self.nodes:
            raise GraphicalErrorNoExistance(name1)
        if name2 not in self.nodes:
            raise GraphicalErrorNoExistance(name2)
        self.edges[name1] = (name1, name2, weight)
        self.edges[name2] = (name2, name1, weight)


    def add_unidirection(self, name1, name2, weight=1):
        """
        Add an unidirectional road between node 1 and node 2
        name1 = name of node 1
        name2 = name of node 2
        weight = weight of path between
        """
        if name1 not in self.nodes:
            raise GraphicalErrorNoExistance(name1)
        if name2 not in self.nodes:
            raise GraphicalErrorNoExistance(name2)
        self.edges[name1] = (name1, name2, weight)  

    
    def delete_node(self, name):
        """
        Delete the node from the graph
        name = name of the node
        """
        




