# Introductoin:

"""
🟢 LEVEL 0.1 — What is Data Structure & Algorithm?

1️⃣ What is a Data Structure?
📌 Simple Definition

A Data Structure is a way of organizing and storing data in memory so that it can be used efficiently.

Data Structures answer the question:
“How should data be stored so operations on it are fast and easy?”

2️⃣ What is an Algorithm?
📌 Simple Definition

An Algorithm is a step-by-step procedure to solve a problem.

Algorithms answer the question:
“What steps should I follow to solve this problem correctly and efficiently?”
"""

# eg of algotihm:


def main():
    print(max_value([5, 3, 25, 78, 19, 6, -81]))


def max_value(li):
    max_val = li[0]
    for i in li:
        if i >= max_val:
            max_val = i
    return max_val


if __name__ == "__main__":
    main();
