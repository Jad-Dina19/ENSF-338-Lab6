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

def search_array(arr, vector):
    for x in vector:
        binary_search(arr, x)

def time_bst(vector):
    tree = build_tree(vector)
    time = timeit(lambda : search_tree(tree, vector), number=10)
    avg_time = time / 10
    print(f"Binary Search Tree: Total Time => {time}, => Average Time {avg_time}")

def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == value):
            return True
        elif (arr[mid] < value):
            left = mid + 1
        elif (arr[mid] > value):
            right = mid - 1
    
    return False
    
def time_bin(vector):
    sorted_vector = vector.copy()
    sorted_vector.sort()
    time_bin = timeit(lambda : search_array(sorted_vector, vector), number=10)
    avg_time = time_bin / 10
    print(f"Binary Search: Total Time => {time_bin}, => Average Time {avg_time}")


def main():
    vector = generate_shuffled_vector()
    time_bin(vector)
    time_bst(vector)


if __name__ == "__main__":
    main()   


"""
Performing a binary search on an array is slightly faster than searching in a binary tree.

While both algorithms have a time complexity of O(log n), data is accessed faster in an array because the data  
are stored next to each other in the memory ensuring fast access.

BST requires traversal from one node pointer to the next. This makes BST slower in practice in comparison with 
arrays.
"""