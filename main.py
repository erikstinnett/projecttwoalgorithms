from timsort import *
from color import *
import random



# INCLUDE OTHER SORTING METHODS BELOW TIMSORT. 
# Use different color to denote sorting method :) 
# for example, Timsort == purple

# Array generation:
# Random integer between 1 and 100,000
arr = [random.randint(1,100000) for _ in range(100)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))



# Array of length 100
# print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
timSort(arr)
print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))
# Include quick, merge, etc. here



# Array of length 1000
arr = [random.randint(1,100000) for _ in range(1000)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
print(arr[:10])
# Timsort array testing
print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
timSort(arr) 
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))



# Array of length 10,000
arr = [random.randint(1,100000) for _ in range(10000)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
print(arr[:10])
# Timsort array testing
print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
timSort(arr) 
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))



# Array of length 100,000
arr = [random.randint(1,100000) for _ in range(100000)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
print(arr[:10])
# Timsort array testing
print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
timSort(arr) 
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))



# Array of length 1,000,000
arr = [random.randint(1,100000) for _ in range(1000000)]

print(color.PURPLE + "\n\nUnsorted array of size N = " + str(len(arr)) + color.END)
print(arr[:10])
# Timsort array testing
print(color.PURPLE +"\nTimsorted Array of size N = " + str(len(arr)) + color.END)
timSort(arr) 
print("First 10 integers: " + str(arr[:10]) + "\nLast 10 integers: " + str(arr[-10:]))