class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def level_order(node):
    queue = [node]
    result = []
    while queue:
        if queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    print(result)

def inverse_level_order(node):
    queue = [node]
    result = []
    while queue:
        if queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    result.reverse()
    print(result)

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    level_order(root)
    print("---")
    inverse_level_order(root)