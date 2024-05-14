# Minimum-Vertex-Cover
This repository is for my Discrete Mathematics Final Project for creating a program to find the minimum vertex cover of a graph.

### Vertex Cover
A vertex cover of a graph 𝐺 is a set, 𝑉𝑐, of vertices in 𝐺 such that every edge of 𝐺 has at least one of vertex in 𝑉𝑐 as an endpoint. This means that every vertex in the graph is touching at least one edge.

## Characterization of MVC (TBU)

- A minimum vertex cover in a graph is a subset of vertices such that every edge in the graph is incident to at least one vertex in the subset. In other words, it is the smallest set of vertices that covers all the edges in the graph.

### **Proof:**

To prove that a set of vertices is a minimum vertex cover, we need to show two things:
- Covering Property: Every edge in the graph is incident to at least one vertex in the subset.
- Minimality: There is no smaller set of vertices that covers all the edges in the graph.
  
### Calculating a Vertex Cover - Implementation Explanation

- What we have: arbitrary conflict graph
    - V - objects
    - E - relationships (e.g. conflict, crossing, overlap)
- What we want: an algorithm to find minimum vertex cover
- Code Logic in Finding Minimum Vertex Cover:

The code provided implements a method to find the minimum vertex cover in a graph using a binary search algorithm combined with dynamic programming. Here's how it works:

**Graph Representation**: The graph is represented using an **adjacency matrix** (gr) to efficiently check edge connectivity and manipulate graph structure.

**isCover** Covering Property Validation Function: This function checks if a given set of vertices forms a vertex cover of size k. It utilizes dynamic programming and uses **bit manipulation** to efficiently generate and check subsets of vertices for covering all edges in the graph.

- iterates through all possible subsets of vertices of size **`k`**
- checks if they cover all the edges in the graph

**findMinCover** Minimality Validation Function: The algorithm employs a **binary search** approach to find the minimum vertex cover size. By iteratively narrowing down the search space, it efficiently determines the smallest possible cover.

- starts with the smallest possible cover size (**`left = 1`**) and the largest possible cover size (**`right = n`**, where **`n`** is the total number of vertices).
- repeatedly calls the **`isCover`** function to check if a cover of size **`mid`** exists. If it does, it updates the **`right`** boundary to **`mid`**, otherwise, it updates the **`left`** boundary to **`mid + 1`**.
