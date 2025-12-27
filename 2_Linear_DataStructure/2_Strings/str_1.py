# String:

"""
Docstring for str_1

1️⃣ What is a String?
📌 Simple Definition

A string is a sequence of characters used to represent text.

2️⃣ Strings Are IMMUTABLE (Most Important Concept)
❗ What does Immutable Mean?

Once a string is created, it cannot be changed.
"""

s = "hello";

print(s[0]); #accessing string element;

#as str is immutuabel:

# s[0] = "c";#error

"""
Why?

Python does not allow modification of string characters

Any “change” creates a new string in memory

🧠 Real-World Analogy

Think of a string as text printed on paper:

You cannot erase one letter

You must print a new page
"""

# Str vs list:

s = "abc";

s = s + "d";#creates new string in the memory
print(s);

li = ["a","b","c"];
li.append("d");#mutate same list

"""
4️⃣ Internal Working (Simplified)

Internally:

Strings are stored as arrays of characters

But Python locks them from modification

This improves:

Security

Performance (hashing)

Predictability
"""

# Common string operations:

# access char:

print(s[1]);#time O(1)

# traverse str: time O(n)

for char in s:
    print(char);

# slicing

print(s[0:2]);#time O(m): m is slice length

"""
6️⃣ Why String Concatenation in Loops Is Dangerous
❌ Bad Practice

⏱ O(n²)
(New string created every iteration)
"""

str_1 = "";

for char in li:
    str_1 = str_1 + char;

print(str_1);

#correct way abnve

str_2 = [];

for char in li:
    str_2.append(char);

str_3 = "".join(str_2);
print(str_3);

"""
7️⃣ Strings in Interviews (Very Important)

Most string problems are about:

Traversal

Frequency counting

Two-pointer technique

Sliding window
"""

# check if str palidorm: time O(n), space O(1)

def is_palindrome(str):
    left, right = 0, len(str) -1;
    while left < right:
        if str[left] != str[right]:
            return False;
        left = left + 1;
        right = right - 1;
    return True;

print(is_palindrome("level"));
print(is_palindrome("abcde"));
print(is_palindrome("madam"));
print(is_palindrome("radar"));