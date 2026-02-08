# Assignment 3 – Algorithm Efficiency and Scalability

##  Overview

This project analyzes the efficiency and scalability of two fundamental algorithms:

- **Randomized Quicksort** (compared with Deterministic Quicksort)
- **Hash Table with Chaining** for collision resolution

The goal is to evaluate both theoretical performance and empirical behavior under different input conditions.

Randomized Quicksort demonstrates how randomization reduces worst-case scenarios in divide-and-conquer algorithms, while Hash Tables with Chaining illustrate efficient handling of collisions in dynamic data structures.

---

##  Project Structure
```
├── randomized_quicksort.py
├── hash_table_chaining.py
├── Assignment_3_Analysis_Report.pdf
└── README.md
```

---

##  File Descriptions

### randomized_quicksort.py
Implements:
- Randomized Quicksort
- Deterministic Quicksort (first-element pivot)
- Runtime comparisons on different input types

### hash_table_chaining.py
Implements a hash table using chaining with:
- Insert
- Search
- Delete operations

---

##  How to Run the Code

### Requirements
- Python 3.x

### Run Randomized Quicksort

python randomized_quicksort.py

### Run Hash Table with Chaining

python hash_table_chaining.py

##  Experiments Performed
Quicksort Comparisons
Random arrays

Sorted arrays

Reverse-sorted arrays

Arrays with repeated elements

Hash Table Evaluation
Insert, search, and delete operations

Impact of collisions and load factor

##  Key Findings
Randomized Quicksort consistently achieves O(n log n) average performance

Deterministic Quicksort performs poorly on sorted inputs

Hash Tables with chaining provide efficient collision handling

Load factor significantly affects performance

##  Concepts Covered

Randomized algorithms

Divide and conquer

Expected time complexity

Hashing and collision resolution

Load factor

##  Author

Pranavi Balakulla

Course: MSCS 532 – Algorithms and Data Structures

##  Notes

Execution times may vary based on system performance
