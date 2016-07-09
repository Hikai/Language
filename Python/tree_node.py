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
    node_child_left = None
    node_child_right = None
    node_parent = None

    def __init__(self, data):
        """Node class init method."""
        self.data = data

    def __del__(self):
        """Node class del method."""
        self.data = None
        if self.node_child_left is not None:
            self.node_parent.node_child_left = self.node_child_left
        if self.node_child_right is not None:
            self.node_parent.noed_child_right = self.node_child_right
        self.node_child_right.node_parent = self.node_parent
        self.node_child_left.node_parent = self.node_parent
        self.node_parent = None

    def set_child_left(self, node):
        """Child node left settings."""
        self.node_child_left = node

    def set_child_right(self, node):
        """Child node right settings."""
        self.node_child_right = node

    def set_parent(self, node):
        """Parent node settings."""
        self.node_parent = node


def main():
    """Main."""
    node1 = Node(123)
    node2 = Node(321)
    node3 = Node(132)
    node4 = Node(231)
    node2.set_parent(node1)
    node2.set_child_left(node3)
    node2.set_child_right(node4)
    del node1

if __name__ == "__main__":
    main()
