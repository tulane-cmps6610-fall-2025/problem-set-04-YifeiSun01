# CMPS 6610 Problem Set 04
## Answers

**Name:**_________Yifei Sun________________


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

| File         | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length |
|---------------|--------------------:|----------------:|--------------------------:|
| alice29.txt   | 1,039,367 | 676,374 | 0.651 |
| asyoulik.txt  | 876,253   | 606,448 | 0.692 |
| f1.txt        | 1,340     | 826     | 0.616 |
| fields.c      | 78,050    | 56,206  | 0.720 |
| grammar.lsp   | 26,047    | 17,356  | 0.666 |

| File         | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length | Entropy H(X) (bits/char) | Huffman Avg Length (bits/char) |
|---------------|--------------------:|----------------:|--------------------------:|--------------------------:|-------------------------------:|
| alice29.txt   | 1,039,367 | 676,374 | 0.651 | 4.513 | 4.555 |
| asyoulik.txt  | 876,253   | 606,448 | 0.692 | 4.808 | 4.845 |
| f1.txt        | 1,340     | 826     | 0.616 | 3.035 | 3.082 |
| fields.c      | 78,050    | 56,206  | 0.720 | 5.008 | 5.041 |
| grammar.lsp   | 26,047    | 17,356  | 0.666 | 4.632 | 4.664 |

Huffman coding is consistently more efficient than fixed-length coding, and the more skewed the character distribution (lower entropy), the greater the compression benefit.



- **1d.**

In the case of all letters in the document having the same frequency, the Huffman tree is almost a balanced binary tree, so all letters basically have the same fixed length of coding, which is $\log_2 \(\lvert \Sigma \rvert\)$ (the cardinality of the alphabet). The expected cost is $N \log_2 \(\lvert \Sigma \rvert\)$, in which $N$ is the number of all letters in the document. It is consistent across all documents as long as the number of letters is the same and all letters have the same frequency.



- **2a.**

To build a binary min-heap in O(n) work, treat the input array as a nearly complete binary tree and restore the heap property from the bottom up.
Treat the array A of length n as an almost-complete binary tree. For 1-based indexing, children of i are 2i and 2i+1 and non-leaf indices are i = ⌊n/2⌋, …, 1. For 0-based indexing, children of i are 2i+1 and 2i+2 and non-leaf indices are i = ⌊(n−2)/2⌋, …, 0.
Starting from the last non-leaf node (at index ⌊n/2⌋−1), perform a sift-down operation on each node: compare it with its children, swap with the smaller child if necessary, and continue until the node is smaller than both children.
Because lower nodes require fewer moves and higher nodes are fewer in number, the total work across all nodes sums to O(n).

At distance h from the leaves (i.e., nodes whose subtree height is h), the number of nodes is at most $n/2^{h+1}$. A sift-down starting at any such node can move down at most $h$ levels, so its cost is at most $c h$ for a constant $c$. Summing over all heights yields a total work bound.

Let $H = \lfloor \log_2 n \rfloor$. The total work satisfies
$$T(n) \le \sum_{h=0}^{H} \frac{n}{2^{h+1}} c h = \frac{c n}{2} \sum_{h=0}^{H} \frac{h}{2^h}.$$

We now compute the finite sum by telescoping.

Define the partial sums
$$S_H = \sum_{h=0}^{H} \frac{h}{2^h}.$$

Multiply by one half and shift the index
$$\frac{S_H}{2} = \sum_{h=0}^{H} \frac{h}{2^{h+1}} = \sum_{k=1}^{H+1} \frac{k-1}{2^{k}}.$$

Subtract
$$S_H - \frac{S_H}{2} = \sum_{h=0}^{H} \frac{h}{2^h} - \sum_{k=1}^{H+1} \frac{k-1}{2^{k}}.$$

Separate the boundary terms and combine like indices
$$\frac{S_H}{2} = \sum_{k=1}^{H} \left(\frac{k}{2^{k}} - \frac{k-1}{2^{k}}\right) - \frac{H}{2^{H+1}} = \sum_{k=1}^{H} \frac{1}{2^{k}} - \frac{H}{2^{H+1}}.$$

Evaluate the geometric sum
$$\sum_{k=1}^{H} \frac{1}{2^{k}} = 1 - \frac{1}{2^{H}}.$$

Therefore
$$\frac{S_H}{2} = 1 - \frac{1}{2^{H}} - \frac{H}{2^{H+1}} = 1 - \frac{H+2}{2^{H+1}},$$
so
$$S_H = 2 - \frac{H+2}{2^{H}}.$$

Plug back into the work bound
$$T(n) \le \frac{c n}{2}\left(2 - \frac{H+2}{2^{H}}\right) = c n - \frac{c n}{2}\cdot \frac{H+2}{2^{H}} < c n.$$

Since $H = \lfloor \log_2 n \rfloor$ and $2^{H} = \Theta(n)$, we conclude
$$T(n) = O(n).$$



- **2b.**

Let the binary heap have height $H = \lfloor \log_2 n \rfloor$.

In level-synchronous construction, all nodes at the same depth $\ell$ perform SIFT-DOWN in parallel.
A node at depth $\ell$ has height $H - \ell$, so its SIFT-DOWN takes $O(H - \ell)$ time.

The total span is the sum of the times for all levels:

$$
T_{span} = \sum_{\ell=0}^{H-1} O(H - \ell)
$$

This is an arithmetic series:

$$
T_{span} = O(1 + 2 + \dots + H) = O(H^2)
$$

Since $H = O(\log n)$, we obtain

$$
T_{span} = O((\log n)^2)
$$

The only difference from the above work calculation is that for every level we are only summing up over one node, not all nodes on that level. 

- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
