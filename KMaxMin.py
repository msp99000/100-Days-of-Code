# Find the "Kth" max and min element of an array
# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]

a = [7, 10, 4, 3, 20, 15]
s = 3
print(kthSmallest(a, s))
