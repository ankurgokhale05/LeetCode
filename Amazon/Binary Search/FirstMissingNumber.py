'''
The Question is to find missing number in sorted array. Here the array is 
ar = [1,2,3,4,6,7,8]
Output: The missing number is 5
The Brute Force approach is to do a linear search.
Optimized approach is to do a binary search
'''

def search(ar, size): 
    left = 0
    right = len(ar) - 1 
    while (right - left) >= 2:
        mid = left + (right - left) // 2
        midIdxDiff = ar[mid] - mid
        leftIdxDiff = ar[left] - left
        rightIdxDiff = ar[right] - right
        if midIdxDiff != leftIdxDiff:
            right = mid
        else:
            left = mid
    return (ar[left] + ar[right]) // 2
  
# Driver Code 
ar = [1,2, 3, 4, 6,7, 8] 
n = len(ar) 
  
print("Missing number:", search(ar, n))