# CMPS 6610 Problem Set 04
## Answers

**Name:**_________________________


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

\begin{table}[h!]
\centering
\begin{tabular}{lrrr}
\hline
\textbf{File} & \textbf{Fixed-Length Coding} & \textbf{Huffman Coding} & \textbf{Huffman / Fixed-Length} \\
\hline
alice29.txt   & 1,039,367 & 676,374 & 0.651 \\
asyoulik.txt  &   876,253 & 606,448 & 0.692 \\
f1.txt        &     1,340 &     826 & 0.616 \\
fields.c      &    78,050 &  56,206 & 0.720 \\
grammar.lsp   &    26,047 &  17,356 & 0.666 \\
\hline
\end{tabular}
\caption{Comparison of fixed-length and Huffman coding costs for five text files.}
\end{table}

\begin{table}[h!]
\centering
\begin{tabular}{lrrrrr}
\hline
\textbf{File} & \textbf{Fixed-Length Coding} & \textbf{Huffman Coding} & 
\textbf{Huffman / Fixed-Length} & \textbf{Entropy $H(X)$ (bits/char)} & 
\textbf{Huffman Avg. Length (bits/char)} \\
\hline
alice29.txt   & 1,039,367 & 676,374 & 0.651 & 4.513 & 4.555 \\
asyoulik.txt  &   876,253 & 606,448 & 0.692 & 4.808 & 4.845 \\
f1.txt        &     1,340 &     826 & 0.616 & 3.035 & 3.082 \\
fields.c      &    78,050 &  56,206 & 0.720 & 5.008 & 5.041 \\
grammar.lsp   &    26,047 &  17,356 & 0.666 & 4.632 & 4.664 \\
\hline
\end{tabular}
\caption{Fixed-length and Huffman coding performance with entropy and average code length. Huffman coding is consistently more efficient than fixed-length coding, and lower entropy (more skewed distributions) leads to greater compression benefits.}
\end{table}

Huffman coding is consistently more efficient than fixed-length coding, and the more skewed the character distribution (lower entropy), the greater the compression benefit.



- **1d.**





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
