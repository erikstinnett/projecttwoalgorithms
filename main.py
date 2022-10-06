from timsort import *
from color import *
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
tic = time.perf_counter()
timSort(arr)
toc = time.perf_counter()
f.write(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"Time taken: {toc - tic:0.6f} seconds" + color.END)
# Include quick, merge, etc. here


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 1000
arr = [random.randint(1,100000) for _ in range(1000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(arr[:10])
# Timsort array testing
f.write(color.PURPLE +"\nAverage Case: Timsorted Array of size N = " + str(len(arr)) + color.END)
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"Time taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 10,000
arr = [random.randint(1,100000) for _ in range(10000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(arr[:10])
# Timsort array testing
f.write(color.PURPLE +"\nAverage Case: Timsorted Array of size N = " + str(len(arr)) + color.END)
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"Time taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 100,000
arr = [random.randint(1,100000) for _ in range(100000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(arr[:10])
# Timsort array testing
f.write(color.PURPLE +"\nAverage Case: Timsorted Array of size N = " + str(len(arr)) + color.END)
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"Time taken: {toc - tic:0.6f} seconds" + color.END)


#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
# Array of length 1,000,000
arr = [random.randint(1,100000) for _ in range(1000000)]

f.write(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
f.write(arr[:10])
# Timsort array testing
f.write(color.PURPLE +"\nAverage Case: Timsorted Array of size N = " + str(len(arr)) + color.END)
tic = time.perf_counter()
timSort(arr) 
toc = time.perf_counter()
f.write("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
f.write(color.UNDERLINE + f"Time taken: {toc - tic:0.6f} seconds" + color.END)
#print(color.BOLD + color.DARKCYAN + '===========================================================================================' + color.END)
