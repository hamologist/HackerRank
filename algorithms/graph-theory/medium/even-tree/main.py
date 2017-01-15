import fileinput

class Tree:
    def __init__(self):
        self.nodes = []
        self.num_of_edges_removed = 0

    def add_nodes(self, num_of_nodes):
        self.nodes = [Node() for x in range(0, num_of_nodes)]

    def count_subtree(self, node):
        children = node.children
        count = len(children)
        for child in children:
            count += self.count_subtree(child)

        return count

    def make_even_tree_forest(self, head):
        children = head.children
        for child in children:
            count = self.count_subtree(child) + 1
            if count and count % 2 == 0:
                self.num_of_edges_removed += 1
            self.make_even_tree_forest(child)


class Node:
    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)


lines = [
    list(
        map(int, line.strip().split(' '))
    ) for line in fileinput.input()
]
N, M = lines.pop(0)
tree = Tree()
tree.add_nodes(N)

for line in lines:
    tree.nodes[line[1]-1].add_child(tree.nodes[line[0]-1])

tree.make_even_tree_forest(tree.nodes[0])
print(tree.num_of_edges_removed)
