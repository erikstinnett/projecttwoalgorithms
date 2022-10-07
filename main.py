from timsort import *
from color import *
from sorts import *
import time

import random

f = open("output.txt", "w")
# INCLUDE OTHER SORTING METHODS BELOW TIMSORT. 
# Use different color to denote sorting method :) 
# for example, Timsort == purple

# Array generation:
# Random integer between 1 and 100,000
arr = [random.randint(1,100000) for _ in range(100)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))


#f.write(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 100
# print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
#-- Tim Sort --
print("\nTim Sorting 100")
tic = time.perf_counter()
timSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Merge Sort --
arr = [random.randint(1,100000) for _ in range(100)]
print("\nMerge Sorting 100")
tic = time.perf_counter()
mergeSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\n\nMergeSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Bubble Sort --
arr = [random.randint(1,100000) for _ in range(100)]
print("\nBubble Sorting 100")
tic = time.perf_counter()
bubbleSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\n\nBubbleSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Quick Sort --
arr = [random.randint(1,100000) for _ in range(100)]
print("\nQuick Sorting 100")
tic = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
toc = time.perf_counter()
f.write(color.PURPLE +"\n\nQuickSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 1000
arr = [random.randint(1,100000) for _ in range(1000)]

f.write("\n\nUnsorted array of size N = " + str(len(arr)))
f.write("\n" + str(arr[:10]))
f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(str(arr[:10]))

#-- Timsort array testing --
f.write("\nAverage Case: Timsorted Array of size N = " + str(len(arr)))
print("\nTim Sorting 1000")
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(f"Time taken: {toc - tic:0.6f} seconds")
f.write("\nFirst 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Merge Sort --
arr = [random.randint(1,100000) for _ in range(1000)]
print("\nMerge Sorting 1000")
tic = time.perf_counter()
mergeSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nMergeSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Bubble Sort --
arr = [random.randint(1,100000) for _ in range(1000)]
print("\nBubble Sorting 1000")
tic = time.perf_counter()
bubbleSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nBubbleSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Quick Sort --
arr = [random.randint(1,100000) for _ in range(1000)]
print("\nQuick Sorting 1000")
tic = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
toc = time.perf_counter()
f.write(color.PURPLE +"\nQuickSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 10,000
arr = [random.randint(1,100000) for _ in range(10000)]

f.write("\n\nUnsorted array of size N = " + str(len(arr)))
f.write("\n" + str(arr[:10]))

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(str(arr[:10]))

#-- Timsort array testing --
f.write(color.PURPLE +"\nAverage Case: Timsorted Array of size N = " + str(len(arr)))
print("\nTim Sorting 10000")
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("\nFirst 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Merge Sort --
arr = [random.randint(1,100000) for _ in range(10000)]
print("\nMerge Sorting 10000")
tic = time.perf_counter()
mergeSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nMergeSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Bubble Sort --
arr = [random.randint(1,100000) for _ in range(10000)]
print("\nBubble Sorting 10000")
tic = time.perf_counter()
bubbleSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nBubbleSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Quick Sort --
arr = [random.randint(1,100000) for _ in range(10000)]
print("\nQuick Sorting 10000")
tic = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
toc = time.perf_counter()
f.write(color.PURPLE +"\nQuickSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 100,000
arr = [random.randint(1,100000) for _ in range(100000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(str(arr[:10]))

#-- Timsort array testing --
f.write("\nAverage Case: Timsorted Array of size N = " + str(len(arr)))
print("\nTim Sorting 100000")
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("\nFirst 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Merge Sort --
arr = [random.randint(1,100000) for _ in range(100000)]
print("\nMerge Sorting 100000")
tic = time.perf_counter()
mergeSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nMergeSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Bubble Sort --
arr = [random.randint(1,100000) for _ in range(100000)]
print("\nBubble Sorting 100000")
tic = time.perf_counter()
bubbleSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nBubbleSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Quick Sort --
arr = [random.randint(1,100000) for _ in range(100000)]
print("\nQuick Sorting 100000")
tic = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
toc = time.perf_counter()
f.write(color.PURPLE +"\nQuickSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 1,000,000
arr = [random.randint(1,100000) for _ in range(1000000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(str(arr[:10]))

#-- Timsort array testing --
f.write("\nAverage Case: Timsorted Array of size N = " + str(len(arr)))
print("\nTim Sorting 1000000")
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("\nFirst 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Merge Sort --
arr = [random.randint(1,100000) for _ in range(1000000)]
print("\nMerge Sorting 1000000")
tic = time.perf_counter()
mergeSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nMergeSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Bubble Sort --
arr = [random.randint(1,100000) for _ in range(1000000)]
print("\nBubble Sorting 1000000")
tic = time.perf_counter()
bubbleSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nBubbleSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)

#-- Quick Sort --
arr = [random.randint(1,100000) for _ in range(1000000)]
print("\nQuick Sorting 1000000")
tic = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
toc = time.perf_counter()
f.write(color.PURPLE +"\nQuickSorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"\nTime taken: {toc - tic:0.6f} seconds" + color.END)
#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
