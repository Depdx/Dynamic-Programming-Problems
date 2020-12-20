class Node:
    """
    Node in graph, contain a box
    :param name : name of the node
    """

    def __init__(self, name: str):
        self.__name = name
        self.connected_node = []

    @property
    def name(self):
        return self.__name

    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError
        self.connected_node.append(node)
