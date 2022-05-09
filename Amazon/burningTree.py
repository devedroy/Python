from collections import deque
import queue


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.root = None

class BurningTree:
    def __init__(self) -> None:
        self.root = None
    
    queue = deque([])

    def burningTree(self, root, targetNode):
        if root is None:
            return 0
        if root.data == targetNode:
            print(root.data)
            