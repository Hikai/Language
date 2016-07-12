# -*- coding: utf-8 -*-
"""
Node(Tree data-structure) class example.

To-do:
"""


class Store:
    """Tree store class."""

    node_root = None

    def __init__(self):
        """Store class init method."""
        pass

    def __del__(self):
        """Store class del method."""
        pass


class Node:
    """Node class."""

    data = None
    depth = None
    node_parent = None
    node_child = []

    def __init__(self, data, depth):
        """
        Node class init method.

        data: Node data
        depth: Node depth
        ex) node_name = Node(data, depth)
        """
        self.data = data
        self.depth = depth

    def __del__(self):
        """Node class del method."""
        self.data = None
        self.node_parent = None

    def set_parent(self, node):
        """Parent node settings."""
        self.node_parent = node

    def add_child(self, *node):
        """Child node add."""
        for child in node:
            self.node_child.append(child)

    def get_child_data(self):
        """Get child node."""
        child_data = []
        for node in self.node_child:
            child_data.append(node.data)
        return child_data

    def get_parent_data(self):
        """Get parent node."""
        return self.node_parent.data


def main():
    """Main."""
    node1 = Node(1, 1)
    node2 = Node(2, 2)
    node3 = Node(3, 2)
    node2.set_parent(node1)
    node3.set_parent(node1)
    node1.add_child(node2, node3)
    print(node1.get_child_data())
    del node3
    del node2
    del node1

if __name__ == "__main__":
    main()
