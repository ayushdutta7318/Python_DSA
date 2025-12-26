# Time Complexity:

"""
Docstring for TimeComplexity_2:

2️⃣ What is Time Complexity?
📌 Definition (Beginner Friendly)

Time Complexity measures how the running time of an algorithm grows as input size grows.

❗ It is NOT actual seconds
❗ It is growth rate
"""

# Diff time complexities;

# 1. O(1): time growth remain constant as i/p grow.

def main():
    print(get_firstEl([5,8,3,1,6]));
    print_all([5,9,55,3,7,99,19]);
    print_pairs([5,9,55,78,46,19,25]);

def get_firstEl(arr):
    return arr[0]; #no matter how larger i/p, time taken remains same.


# 2. O(n): time direct proportn to inp
def print_all(arr):
    for i in range(len(arr)):
        print(f"{i}:{arr[i]}");
    return 0;

# 3. O(n^2): Quadratic time: nested loop:
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(f"{i}:{j}");
    return 0;

if __name__ == "__main__":
    main();