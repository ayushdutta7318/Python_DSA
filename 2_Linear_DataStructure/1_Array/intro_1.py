# Arrays (List) in python:

"""
Docstring for intro_1

🟢 LEVEL 2.1 — Arrays & Python Lists (Deep Dive)
1️⃣ What is an Array?
📌 Simple Definition

An array is a collection of elements stored in contiguous memory locations.

“Contiguous” means next to each other in memory.
"""

# eg:

arr = [1,2,3,4,5];

arr.append(75);

print(arr);

"""
2️⃣ Why Arrays Are Fast
🎯 Direct Access (Random Access)
"""

arr = [45,55,79,84,6,184];

print(arr[2]);# time comp: O(1)

"""
Why?

Memory address = base address + index × size

No searching required
"""

"""
3️⃣ Python Lists vs Arrays (Important Clarification)

Python does not have a traditional fixed-size array by default.

🔹 Python List

1.Dynamic (can grow/shrink)
2.Internally implemented using arrays
3.Over-allocates memory for efficiency

Behind the scenes:
Python may allocate extra space
When full, it creates a bigger array and copies data and empties previous occupied memory.

4️⃣ Common Array Operations & Their Complexity

Let’s analyze every operation carefully.
"""

# Access array eleement:

arr = [45,23,55,3,7,41,51];
print(arr[0]);#time O(1)

# arr traversal: time O(n)
for num in arr:
    print(num);

# Insertion:
# 1. at end: time O(1)

arr.append(99);
print(arr);

# 2. at beginning/middle: O(n) because all element index must shift

arr.insert(0, 777);
print(arr);
arr.insert(round(len(arr)/2), 789);
print(arr);

# deletion:
"""
Elements shift left
⏱ Time Complexity: O(n)
"""

arr.pop(1);
print(arr);

"""
6️⃣ When Should You Use Arrays?
✅ Use Arrays When:

You need fast access

Data size is known or rarely changes

Order matters

Index-based operations are frequent

❌ Avoid Arrays When:

Frequent insertions/deletions at beginning

Unknown or highly dynamic size

Memory movement is costly

7️⃣ Common Beginner Mistakes

❌ Using lists for frequent middle insertions
❌ Assuming append() is always O(1)
❌ Confusing array access with searching
❌ Ignoring time complexity of insert() & pop(0)
"""

"""
8️⃣ Small Practice (Think Before Coding)
Question 🤔

Given a list of n elements, which is faster?

Access the 500th element

Check if number x exists

👉 Think in terms of O(1) vs O(n)
"""

a = [1,2,3,4,5,6,7,8,9,10];

print(a[9]); #time O(1):

def linear_search(arr, targetEl):
    for num in arr:
        if num == targetEl:
            return True;
    return False;


print(linear_search([1,2,3,4,5,6,7,8,9,10], 5));
print(linear_search([1,2,3,4,5,6,7,8,9,10], 5000));