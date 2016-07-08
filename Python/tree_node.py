# -*- coding: utf-8 -*-
"""
Node(Tree data-structure) class example.

To-do:
"""


class Node:
    """Node class."""

    data = None
    node_child = None
    node_parent = None

    def __init__(self, data):
        """Node class init method."""
        self.data = data

    def set_child(self, node):
        """Child node settings."""
        self.node_child = node

    def set_parent(self, node):
        """Parent node settings."""
        self.node_parent = node


def main():
    """Main."""
    node1 = Node(123)
    node2 = Node(321)
    node3 = Node(132)
    node2.set_parent(node1)
    node2.set_child(node3)


if __name__ == "__main__":
    main()
