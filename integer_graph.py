from ac_graph import AcNode

class InputNode(AcNode):
    def __init__(self, graph, data):
        super().__init__(graph)
        self.data = data
        
    def eval(self):
        print(f'Evaluating input node {self.id()}')
        
    def read(self):
        return self.data
    
class AddNode(AcNode):
    def __init__(self, graph, *nodes):
        super().__init__(graph)
        self.data = 0
        for node in nodes:
            self.add_predecessor(node)
    def eval(self):
        print(f'Evaluating addition node {self.id()}')
        for node in self.preds:
            self.data += node.read()
            
    def read(self):
        return self.data
    
class ProductNode(AcNode):
    def __init__(self, graph, *nodes):
        super().__init__(graph)
        self.data = 0
        for node in nodes:
            self.add_predecessor(node)
    def eval(self):
        print(f'Evaluating product node {self.id()}')
        for node in self.preds:
            self.data = self.data * node.read()
            
    def read(self):
        return self.data