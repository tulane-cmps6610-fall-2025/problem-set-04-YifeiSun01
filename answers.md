# CMPS 6610 Problem Set 04
## Answers

**Name:**_________________________


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

In the case of all letters in the document having the same frequency, the Huffman tree is almost a balanced binary tree, so all letters basically have the same fixed length of coding, which is $\log_2 \(\lvert \Sigma \rvert\)$ (the cardinality of the alphabet). The expected cost is $N \log_2 \(\lvert \Sigma \rvert\)$, in which $N$ is the number of all letters in the document.



- **2a.**




- **2b.**




- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
