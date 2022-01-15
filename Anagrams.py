'''
Given two strings s1 and s2. Check if they are anagrams.
Two strings are anagrams if they are made up of same characters with same frequencies
example:
s1 = "danger"
s2 = "garden"
'''

# Solution 1:   O(n)T | O(n)S
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for char in s1:
        if char in freq1:
            freq1[char] +=1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] +=1
        else:
            freq2[char] = 1

    if freq1 == freq2:
        return True
    else:
        return False

# Solutions 2:  O(nlogn)T | O(n)S
def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
