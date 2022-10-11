# code taken from geeks for geeks
# Each sort returns time elapsed

import time

def mergeSort(arr):
    tic = time.perf_counter()
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    toc = time.perf_counter()
    dt = ((toc - tic) * 1000)

    return arr, dt


def bubbleSort(arr):
    tic = time.perf_counter()
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    toc = time.perf_counter()
    dt = ((toc - tic) * 1000)

    return arr, dt

# Function to find the partition position
def partition(array, low, high):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
  
    # Pointer for greater element
    i = low - 1
  
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
  
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    # Return the position from where partition is done
    return i + 1
  
# Function to perform quicksort

def quick_sort(array, low, high):
    #print(f"QS Input Array Length:{len(array)} \n\tLo,Hi = {low},{high}")
    tic = time.perf_counter()
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)

    toc = time.perf_counter()
    dt = ((toc - tic) * 1000)
    #print(f"DeltaT:{dt}")

    return array, dt