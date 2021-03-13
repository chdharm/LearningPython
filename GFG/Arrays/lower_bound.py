def binarySearchLowerBound(arr, start, end, k):
    if start > end:
        return arr[start]
    middle = (end - start)/2 + start

    if arr[middle] >= k:
        return binarySearchLowerBound(arr, start, middle, k)

if __name__ == '__main__':
    n = 6
    li = []
    k = 12
    print(binarySearchLowerBound(li, 0, n))