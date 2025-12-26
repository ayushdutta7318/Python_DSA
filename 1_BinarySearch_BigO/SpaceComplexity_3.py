# Space complexity:

"""
Docstring for SpaceComplexity_3

Space Complexity (Memory Usage)
📌 Definition

Space Complexity measures extra memory used by an algorithm.
"""

def main():
    print(sum(5,5));
    print(copy_list([1,2,3,4,5]));

# 1. O(1): constant memory:

def sum(a: int,b: int)->int:
    return a+b;

# 2. O(n): memory increases as the input increases:

def copy_list(arr):
    new_list = [];
    for el in arr:
        new_list.append(el);
    return new_list;

if __name__ == "__main__":
    main();

"""
8️⃣ Time vs Space Tradeoff

Sometimes:

Faster code uses more memory

Memory-efficient code runs slower

This tradeoff appears constantly in DSA.

🧠 Common Beginner Mistakes

❌ Counting exact steps
❌ Forgetting worst case
❌ Ignoring nested loops
❌ Confusing time with actual seconds
"""

