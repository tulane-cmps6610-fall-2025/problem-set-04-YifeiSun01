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

INPUT: integer N ≥ 0; denominations D = {2⁰, 2¹, …, 2ᵏ}  
OUTPUT: multiset A of coins (values in D) summing to N, with as few coins as possible  

procedure MakeChange(N):  
 A ← ∅  
 for j from k down to 0 do  
  if 2ʲ ≤ N then  
   a ← ⌊ N / 2ʲ ⌋  
   include a coins of value 2ʲ into A  
   N ← N − a · 2ʲ  
  end if  
 end for  
 return A  

 find the largest change of denomination that is smaller than N, use as much of that change as possible and then subtract N by the amount and repeat for the next step using the remaining value of N, use the next biggest change, as much as possible.

- **3b.**

**Proof of optimality**

*Greedy Algorithm:* Given $N$, pick the largest coin value $2^k$ that does not exceed the remaining amount; use as many coins of denomination $2^k$ as possible (i.e. $a = ⌊N / 2^k⌋$), subtract $a·2^k$ from $N$, and repeat on the remainder with the next smaller denomination until the amount is zero.

**1. Greedy-choice property**  
Let the denominations be $1, 2, 4, …, 2^k$.  
Claim: There exists an optimal solution that uses exactly $a = ⌊N / 2^k⌋$ coins of value $2^k$ in its first step.  
*Proof:* Suppose an optimal solution Opt uses $b < a$ coins of value $2^k$, and uses coins of value $≤ 2^{k−1}$ to make up the remainder. Then the remaining amount is  
$$N - b \cdot 2^k \ge N - (a - 1)\cdot2^k \ge 2^k.$$  
Since coins of value at most $2^{k−1}$ cannot sum to $2^k$ using fewer than two coins, replacing those smaller denom­ination coins by one additional $2^k$ coin yields a solution with strictly fewer coins—a contradiction to Opt being optimal. Therefore Opt must use a coins of value $2^k$ in the first step.

**2. Optimal substructure**  
After using a coins of value $2^k$, the remainder is  
$$N' = N - a \cdot 2^k,$$  
and the remaining problem is: make change for N′ using denominations $1, 2, 4, …, 2^{k−1}$.  
Let Opt′ be the coins used by Opt for this remainder. If Opt′ is not optimal for the sub-problem of making change for N′, then there is a better solution S′ using fewer coins. Replacing Opt′ by S′ (and keeping the a coins of value $2^k$) gives a full solution for $N$ with fewer coins than Opt—contradiction. Thus Opt′ must itself be optimal for the sub-problem.  
Hence the problem exhibits the optimal-substructure property.

**Conclusion:** Since both the greedy‐choice property and the optimal‐substructure property hold, the greedy algorithm always produces an optimal (minimum-coin) solution for making change when coin denominations are powers of 2.


- **3c.**

**Work and Span Analysis**  

Let the denominations be $1, 2, 4, …, 2^k$, and suppose we wish to make change for amount $N$.  
We have $2^k ≤ N < 2^{k+1}$, so $k + 1 = O(log N)$ denominations.

**Work:**  
At each step for denomination 2^i we compute the integer quotient  
$$a_i = \left\lfloor \frac{N_{\rm rem}}{2^i} \right\rfloor$$  
and then update  
$$N_{\rm rem} \leftarrow N_{\rm rem} - a_i \cdot 2^i.$$  
There are k + 1 steps and each step takes O(1) arithmetic operations, so  
$$W = O(k) = O(\log N).$$

**Span:**  
In the straightforward sequential implementation, each update depends on the value of $\(N_{\rm rem}\)$ from the previous step. Thus the longest chain of dependencies (the critical path) has length  
$$S = O(k) = O(\log N).$$  
Because span and work are of the same asymptotic order, the parallelism ratio satisfies  
$$\frac{W}{S} = O(1)$$  
so the algorithm is essentially sequential and cannot exploit significant parallelism.

**Conclusion:**  
Work = $\(W = O(\log N)\)$ and Span = $\(S = O(\log N)\)$.  
Hence this greedy change-making algorithm has limited potential for parallel speed-up.




- **4a.**

Let the denomination set be  
$$D = \{1, 3, 4\}$$  
and let the target amount be  
$$N = 6.$$

**Greedy algorithm execution:**  
1. Choose the largest coin value ≤ 6, which is 4. Then remaining = 6 − 4 = 2.  
2. Choose the largest coin value ≤ 2, which is 1. Then remaining = 2 − 1 = 1.  
3. Choose the largest coin value ≤ 1, which is 1. Then remaining = 1 − 1 = 0.  
Total coins used by greedy = 3.

**Optimal solution:**  
Use two coins of value 3 each: 3 + 3 = 6.  
Total coins used = 2.

Since 3 (greedy) > 2 (optimal), the greedy algorithm does **not** yield the fewest coins in this case.  
Thus the greedy algorithm fails for this denomination set.

Another example:

Let the denomination set be  
$$D = \{1, 35, 40\}$$  
and let the target amount be  
$$N = 70.$$

greedy algorithm would take 1 40 and 30 1.

the best way is 2 35.

In this setting of a completely random set of coins' denomination, we can not even make the value N. For example if all coins' denominations are even and the value is odd.

- **4b.**

**Claim (Optimal substructure).**
Let D be the set of denominations. Define OPT(n) as the minimum number of coins needed to form value n,
and take OPT(n)=+∞ if n cannot be formed. Then for n≥1:

$$\mathrm{OPT}(n)=\min_{d\in D,\ d\le n}\ \{\,1+\mathrm{OPT}(n-d)\,\},\quad \mathrm{OPT}(0)=0.$$

Equivalently, any optimal solution for n can be obtained by choosing one coin d∈D with d≤n and then
extending an optimal solution for n−d by that coin.

**Proof.**
Fix n≥1. If n is infeasible, then for every d≤n either n−d is infeasible or adding d overshoots, so the
right-hand side is +∞, matching OPT(n)=+∞.

Otherwise let S be an optimal multiset of coins summing to n with |S|=OPT(n). Take any coin d∈S and
let S′=S\{d}. Then S′ sums to n−d, so OPT(n−d)≤|S′|=OPT(n)−1, hence

$$\mathrm{OPT}(n)\ge 1+\mathrm{OPT}(n-d).$$

Since this holds for the particular d∈S, it holds for the minimum over all d≤n, giving

$$\mathrm{OPT}(n)\ge \min_{d\le n}(1+\mathrm{OPT}(n-d)).$$

For the reverse inequality, pick any d∈D with d≤n and any optimal multiset T for n−d, with |T|=OPT(n−d).
Then T∪{d} forms n using 1+OPT(n−d) coins, so

$$\mathrm{OPT}(n)\le 1+\mathrm{OPT}(n-d).$$

Taking the minimum over d≤n yields

$$\mathrm{OPT}(n)\le \min_{d\le n}(1+\mathrm{OPT}(n-d)).$$

Combining both directions proves the recurrence and thus the optimal substructure.


- **4c.**

pseudo code of a bottom up method

function MinCoins(x):

    if x = 0 then
        return 0
    if x < 0 then
        return +∞          // not possible to make negative amount
    if memo[x] ≠ “UNCOMPUTED” then
        return memo[x]

    best = +∞
    for i = 0 to k−1 do
        d = coins[i]
        if x − d ≥ 0 then
            sub = MinCoins(x − d)
            if sub ≠ +∞ then
                best = min(best, sub + 1)
            end if
        end if
    end for

    memo[x] = best
    return best
end function

store all results for the imtermediate steps and subproblems, the number of coins and what coins in the results, retrieve the result whenever you encounter the state from the stored results

Let N be the target and k the number of coin types.

Work:
Each state x ∈ {1..N} is computed once, and for that state we scan up to k coin types.
Total work = Θ(kN).

Span:
The dependency DAG goes from x to x−d. The longest dependency chain has length equal to the minimum number of coins needed for N, which is ≤ N when a 1-coin exists.
If the inner min over k coin choices is done sequentially, span = Θ(N).
If the inner min over k is reduced in parallel, span = Θ(N log k).

- **5a.**

Theorem. Weighted task selection satisfies the optimal substructure property.

Proof.  
Sort all tasks so that f1 ≤ f2 ≤ … ≤ fn. For each task i define  
$$p(i)=\max\{ j<i : f_j \le s_i \}$$  
and let OPT(i) be the maximum total value obtainable from the first i tasks, with OPT(0)=0.

For each i≥1, the optimal value satisfies  
$$OPT(i)=\max\{ v_i + OPT(p(i)), OPT(i-1) \}$$

If task $i$ is not included in the optimal set, the best value is $OPT(i−1)$.  
If task $i$ is included, all compatible tasks must finish before $s_i$, giving total value $v_i + OPT(p(i))$.  
Choosing the larger of the two gives the recurrence.  
Therefore the problem has the optimal substructure property.


- **5b.**

The greedy choice property does not hold in general. Below are two counterexamples showing that natural greedy rules can fail.

Counterexample 1: “earliest finishing time” fails.

Tasks (si, fi, vi):

a1: (0, 3, 4)

a2: (3, 5, 3)

a3: (0, 5, 8)

Greedy by earliest finish picks a1 then a2 with total value 7. The optimal is to pick a3 with value 8.

Counterexample 2: “maximum raw value” fails.

Tasks (si, fi, vi):

b1: (0, 2, 4)

b2: (2, 4, 4)

b3: (0, 4, 7)

Greedy by maximum value picks b3 first (value 7), leaving no room for b1 or b2, achieving total value 7.
The optimal is to pick b1 and b2, achieving total value 8.

Counterexample 3: “maximum value density” fails.

Tasks (si, fi, vi):

c1: (0, 4, 7)    length 4, density 1.75

c2: (4, 10, 7)   length 6, density ≈1.1667

c3: (0, 10, 15)  length 10, density 1.5

Greedy by highest value/length ratio picks c1 first, then c2, for total value 14.
The optimal is to pick only c3 with total value 15.

Conclusion. No single local greedy rule like earliest finish, latest start, highest value, highest value per unit time is guaranteed to be optimal for weighted tasks.


- **5c.**
