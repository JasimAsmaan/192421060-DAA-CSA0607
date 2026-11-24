# Task B1 - Implement and Instrument Your Search

## Graph Colouring

### Marks

7 Marks

---

## 1. Objective

The objective of this task is to implement the backtracking Graph Colouring algorithm designed in Task A1 and experimentally analyse its search behaviour.

The implementation records:

- Search nodes visited
- Candidate assignments attempted
- Branches rejected by the feasibility test
- Number of backtracks
- Maximum search depth
- Final colouring, if one exists

---

## 2. Problem Description

A cloud platform contains several software services.

Each service is represented as a vertex in a graph.

A conflict between two services is represented by an edge.

Each available server group is represented as a colour.

The objective is to determine whether all services can be assigned to server groups such that no two conflicting services are assigned to the same group.

---

## 3. Input

The algorithm requires:

- A graph containing vertices and edges
- Number of vertices
- Number of available colours

---

## 4. Output

The program produces:

- Whether the graph is colourable
- Colour assigned to each vertex
- Search nodes visited
- Candidate assignments attempted
- Rejected branches
- Number of backtracks
- Maximum search depth

---

# B1.1 - Validate the Implementation

The implementation is tested using three different cases.

## Test Case 1 - Colourable Graph

A graph that can be coloured using the specified number of colours.

### Purpose

This test verifies that the algorithm can successfully find a valid colouring.

### Input

Number of colours:

```text
3
