# Insert sort with names in Python

def insertSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

arr = [4, 3, 90, 7, 5, 67, 44, 65, 23, 78, 88, 93, 4, 5, 6, 34, 51, 19]
insertSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])