Dynamic Programming is optimization over plain recursion

dyamic programming conditions:
1. solve problem by solving subproblem
2. you should have repeating subproblems
3. optimal substructure


dynamic programming classification:
 Easy to meadium: (Important for interview)
 1. knapsack -> 
        a. 0-1
        b. Bounded
        c. Unbounded
2. LCS (Longest common subsequence)
3. LIS(Longest increasing subsequence)
4. Matrix chain multiplication
5. DP on grid
6. kadane's algorithm
7. others

Advanced DP(important for competetive programming)
1. DP kth lexicographical string
2. DP on tree
3. DP + Bitmasking
4. DP + BIT(binary index tree)/Segment Tree
5. DP + convex hell
6. DP + pre processing
7. DP + Trie
8. DP + Geometry
9. DP + Binary Search
10. DP + Kuth Optimization
11. others



Knapsack And its classification:
1. Knapsack
2. Types
3. DP
4. Knapsack Variations

What is a knapsack problem?
Knapsack means  a bag.
problem: items with price , profit and weight
goal: fill the bag to get max profit
input: given item with weight and profit

knapsack can be 3 types:
1. 0/1: inclued one item from each not multiple
2. bounded: include multiple instance from same item but finite number of not infinite means has boundary
3. unbounded: include multiple instance from same item but not any boundary
4. Factional(greedy): can include fractional part of item
5. Integer: can't pick factional part an item