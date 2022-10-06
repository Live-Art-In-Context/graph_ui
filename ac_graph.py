
"""ac_graph module: contains the classes AcNode and NanedAcNode.
    Each is the basis of a dead simple acyclic graph.
    Meant to be super class of other data classes to facilitate traversal."""

class AcGraph:
    def __init__(self, name=""):
        self.__next_node_id = 1
        self.__node_list = []
        self.__name = name
    def next_id(self):
        id = self.__next_node_id
        self.__next_node_id += 1
        return id

    def add_node(self, node):
        self.__node_list.append(node)

    def rm_node(self, node):
        print("Not yet implemented: AcGraph.rm_node(.)")

    def node_list(self):
        return self.__node_list

    def name(self):
        return self.__name

class AcNode:
    def __init__(self, graph) -> None:
        self.parent_graph = graph
        self.preds = []
        self.succ = []
        self._id = self.parent_graph.next_id()
        self.parent_graph.add_node(self)

    def predecessors(self):
        return self.preds

    def successors(self):
        return self.succ
    
    def add_predecessor(self, node):
        self.preds.append(node)
        node.succ.append(self)
    
    def add_successor(self, node):
        self.succ.append(node)
        node.preds.append(self)
    
    def id(self):
        return self._id
        
    def node_list(self):
        return self.parent_graph.node_list()

    

class NamedAcNode(AcNode):
    def __init__(self, graph, name="") -> None:
        super().__init__(graph)
        self.name = f'{self._id}' if name=="" else name
    
    def node_name(self):
        return self.name