import sys
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def parse_exp(exp):
    tokens = exp.split()
    root = Node()
    stack = []
    current = root

    for token in tokens:
        if(token == "("):
            current.left = Node()
            stack.append(current)
            current = current.left
        elif(token in ["+", "-", "*", "/", ]):
            current.right = Node()
            current.value = token
            stack.append(current)
            current = current.right
        elif(token == ")"):
            if stack:
                current = stack.pop()
        else:
            current.value = int(token)
            if stack:
                current = stack.pop()

    return root       
            
def post_order_traversal(current):
    result = 0
    if current is None:
        return None
    if(current.left == None and current.right == None ):
        return current.value
    
    if(current.value == "+"):
        left_op = post_order_traversal(current.left)
        right_op = post_order_traversal(current.right)
        
        result = left_op + right_op
    elif(current.value == "-" ):
        left_op = post_order_traversal(current.left)
        right_op = post_order_traversal(current.right)
        
        result = left_op - right_op
    elif(current.value == "*"):
        left_op = post_order_traversal(current.left)
        right_op = post_order_traversal(current.right)
        
        result = left_op * right_op    
    else:
        left_op = post_order_traversal(current.left)
        right_op = post_order_traversal(current.right)
        
        result = left_op / right_op

    return result   

def main():
    tree = parse_exp(sys.argv[1])
    print("Value of Expression:", post_order_traversal(tree))

if __name__ == "__main__":
    main()