def merge(arr, l, m, r):
    n1 = m - l + 1  # Size of the left subarray
    n2 = r - m      # Size of the right subarray

    leftSubarray = [0] * n1
    rightSubarray = [0] * n2

    for x in range(n1):
        leftSubarray[x] = arr[l + x]
    for y in range(n2):
        rightSubarray[y] = arr[m + 1 + y]

    p = 0  # Pointer for the left subarray
    q = 0  # Pointer for the right subarray
    k = l  # Pointer for the merged subarray

    while p < n1 and q < n2:
        if leftSubarray[p] <= rightSubarray[q]:
            arr[k] = leftSubarray[p]
            p += 1
        else:
            arr[k] = rightSubarray[q]
            q += 1
        k += 1

    while p < n1:
        arr[k] = leftSubarray[p]
        p += 1
        k += 1

    while q < n2:
        arr[k] = rightSubarray[q]
        q += 1
        k += 1

def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if l<r:
        mid = l+(r-l)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)
    return arr