def rotated_search(arr, start, end, num):
    if start > end:
        return -1
    mid = start + int((end-start)/2)
    if arr[mid] == num:
        return mid
    if arr[mid] > num:
        if arr[mid] >= arr[start] and arr[start] <= num:
            return rotated_search(arr, start, mid-1, num)
        return rotated_search(arr, mid+1, end, num)

    if arr[mid] <= arr[end] and arr[end] >= num:
        return rotated_search(arr, mid+1, end, num)
    return rotated_search(arr, start, mid-1, num)

if __name__ == '__main__':
    arr = [13, 18, 25, 2, 8, 10]
    print(rotated_search(arr, 0, len(arr)-1, 18))