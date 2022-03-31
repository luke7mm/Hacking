def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

    # QuickSort function

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        #pi = partitioning index

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Driver code to test
arr = [15, 9, 6, 34, 66, 2, 5, 2, 5, 2, 7]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

# Copied from https://www.geeksforgeeks.org/python-program-for-quicksort/
# This code is contributed by Mohit Kumra
# This code in improved by https://github.com/anushkrishnav