import math, queue, os
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    for c in f.keys():
        p.put(TreeNode(None, None, (f[c], c)))
    while p.qsize() > 1:
        x = p.get()
        y = p.get()
        z = TreeNode(x, y, (x.data[0] + y.data[0], ''))
        p.put(z)
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    if node is None:
        return
    if node.left is None and node.right is None:
        code[node.data[1]] = prefix
        return code
    get_code(node.left, prefix + "0", code)
    get_code(node.right, prefix + "1", code)
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    n = len(f)
    bits = math.ceil(math.log2(n))
    total = sum(f.values()) * bits
    return total

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    return sum(len(C[c]) * f[c] for c in f)

def shannon_entropy(f):
    """Shannon entropy H(X) in bits per symbol, from a freq dict f."""
    total = sum(f.values())
    if total == 0:
        return 0.0
    H = 0.0
    for freq in f.values():
        p = freq / total
        H -= p * math.log2(p)
    return H

def avg_code_length_huffman(huff_cost, f):
    total = sum(f.values())
    return (huff_cost / total) if total > 0 else 0.0

def bits_per_symbol_fixed(f):
    n = len(f)
    return math.ceil(math.log2(n)) if n > 0 else 0

def list_txt_files(directory):
    return [f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) and (f.endswith('.txt') or f.endswith('.lsp') or f.endswith('.c'))]

directory = '.'  
txt_files = list_txt_files(directory)
print(txt_files)

for fname in txt_files:
    print("Processing file:", fname)
    f = get_frequencies(fname)

    fixed = fixed_length_cost(f)
    T = make_huffman_tree(f)
    C = get_code(T)
    huff = huffman_cost(C, f)

    # Compute information-theoretic measures
    H = shannon_entropy(f)
    L_huff = avg_code_length_huffman(huff, f)
    b_fixed = bits_per_symbol_fixed(f)

    # Print results
    print("Fixed-length cost:          %d" % fixed)
    print("Huffman cost:               %d" % huff)
    if fixed > 0:
        ratio = huff / fixed
        print("Ratio (Huffman/Fixed):      %.3f" % ratio)
    else:
        print("Ratio (Huffman/Fixed):      N/A (fixed cost = 0)")

    # Information metrics
    print("Entropy H(X):               %.3f bits/char" % H)
    print("Huffman average length:     %.3f bits/char" % L_huff)
    print("Fixed-length bits/symbol:   %d bits/char" % b_fixed)
    print()


