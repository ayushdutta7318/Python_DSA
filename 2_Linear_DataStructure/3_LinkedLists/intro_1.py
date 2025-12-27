# Linked Lists:

"""
Docstring for intro_1

🟢 LEVEL 2.3 — Linked Lists (Beginner → Deep Understanding)
1️⃣ Why Do We Need Linked Lists?
Problem with Arrays (Quick Recall)

Insertion/deletion in middle → O(n) (shifting)

Fixed or expensive resizing

Memory must be contiguous

👉 Linked Lists solve these problems.

2️⃣ What is a Linked List?
📌 Simple Definition

A Linked List is a linear data structure where:

Each element is a node

Each node stores:

Data

Reference (link) to the next node

Nodes are not stored contiguously in memory.
"""
# initiating a node in ll:

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

    #traverse linked list
    def traverse(head):
        current = head;
        while current:
            print(current.data);
            current = current.next;
        #time: O(n), space O(1)
    
    #insertion in ll:

    #insert at beginning
    def insert_at_beginning(head,data):
        new_node = Node(data);
        new_node.next = head;


"""

4️⃣ Singly Linked List
Visual Representation

HEAD
 ↓
[10] → [20] → [30] → None

head stores address of first node
Last node points to None

5️⃣ Why Linked Lists Are Powerful
✅ Advantages

Dynamic size

Efficient insertion/deletion (O(1) if position known)

No memory shifting

No contiguous memory requirement

❌ Disadvantages

No direct indexing

Extra memory for pointers

Traversal is slower than arrays

6️⃣ Traversing a Linked List
Step-by-Step Thinking

Start at head

Visit current node

Move to next

Stop at None
"""

