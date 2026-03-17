from timeit import timeit
import sys 
import random

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, current=None):
        
        if self.root is None:
            self.root = node
            return
        
        if current is None:
            current = self.root
        
        if node.value <= current.value:
            if current.left is None:
                current.left = node
            else:
                self.insert(node, current.left)
        elif node.value > current.value:
            if current.right is None:
                current.right = node
            else:
                self.insert(node, current.right)

    def search(self, value, current=None):
        
        if current is None:
            current = self.root
        
        if current is None:
            return False
        
        if current.value == value:
            return True
        
        if value <= current.value:
            if(current.left is None):
                return False
            else:
                return self.search(value, current.left)
        elif value > current.value:
            if(current.right is None):
                return False
            else:
                return self.search(value, current.right)
            
        
def generate_sorted_vector():
    return list(range(10000))

def generate_shuffled_vector():
    lst = list(range(10000))
    random.shuffle(lst)
    return lst

def build_tree(vector):
    tree = BST()
    
    for x in vector:
        tree.insert(Node(x))

    return tree

def search_tree(tree, vector):
    for x in vector:
        tree.search(x)
    
def time_sorted():
    vector = generate_sorted_vector()
    tree = build_tree(vector)
    time = timeit(lambda : search_tree(tree, vector), number=10)
    avg_time = time / 10
    
    print(f"Sorted: Total Time => {time}, => Average Time {avg_time}")

def time_shuffled():
    vector = generate_shuffled_vector()
    tree = build_tree(vector)
    time = timeit(lambda : search_tree(tree, vector), number=10)
    avg_time = time / 10
    print(f"Shuffled: Total Time => {time}, => Average Time {avg_time}")
    
    
def main():
    time_sorted()
    time_shuffled()


if __name__ == "__main__":
    main()   


"""
The time for the sorted vector is a lot slower than the shuffled vector. This is because the sorted vector
inserts the elements in order, since this vector is ordered ascendingly, every value was always inserted to the very most
right leaf of the tree. This just ends up creating a linked list which has a traversal time of O(n) rather than O(log(n))
like a regular Binary Search Tree.
"""