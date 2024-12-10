class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  
        self.symbol = symbol 
        self.left = left  
        self.right = right 
        
def decode_huff(root, s):
    decoded_str = []
    current_node = root
    
    for char in s:
        if char == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
            
        if current_node.left is None and current_node.right is None:
            decoded_str.append(current_node.symbol)
            current_node = root  
    
    return ''.join(decoded_str)

# Example usage:
root = Node(None, None, 
            left=Node(None, 'B', None, None), 
            right=Node(None, 'A', None, None)
           )

s = "1001011"
decoded_message = decode_huff(root, s)
print(decoded_message)  # Output: ABACA
