class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # character
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # 0 or 1
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def print_nodes(node, val=''):
    # huffman code for current node
    new_val = val + str(node.huff)

    # if node is not an edge node then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Calculate frequency of each character
    symbols = {}
    for char in text:
        if char in symbols:
            symbols[char] += 1
        else:
            symbols[char] = 1

    # Create a list of nodes
    nodes = []
    for symbol, freq in symbols.items():
        nodes.append(Node(freq, symbol))

    # Construct the Huffman Tree
    while len(nodes) > 1:
        # Sort nodes by frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # Pick two nodes with lowest frequency
        left = nodes[0]
        right = nodes[1]

        # Assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # Combine the two lowest nodes to create a new node
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        # Remove the two nodes and add the new node
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    # Return the root of the Huffman Tree
    return nodes[0]


# Function to encode text using the Huffman Tree
def huffman_encoding(text):
    if not text:
        return "", None

    root = build_huffman_tree(text)

    # Dictionary to store codes
    codes = {}

    # Function to traverse the tree and get codes
    def get_codes(node, val=''):
        new_val = val + str(node.huff)

        if node.left:
            get_codes(node.left, new_val)
        if node.right:
            get_codes(node.right, new_val)

        if not node.left and not node.right:
            codes[node.symbol] = new_val

    # Start with empty code initially
    get_codes(root)

    # Generate encoded text
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]

    return encoded_text, root


# Function to decode the encoded text using the Huffman Tree
def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current = root

    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # If leaf node, append the symbol to result and reset to root
        if not current.left and not current.right:
            decoded_text += current.symbol
            current = root

    return decoded_text


# Example usage
if __name__ == "__main__":
    text = input("enter a text")

    # Encoding
    encoded_text, tree = huffman_encoding(text)
    print("Encoded text:", encoded_text)

    # Print the codes
    print("\nHuffman Codes:")
    print_nodes(tree)

    # Decoding
    decoded_text = huffman_decoding(encoded_text, tree)
    print("\nDecoded text:", decoded_text)