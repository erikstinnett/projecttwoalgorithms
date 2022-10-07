# Main implementation file for project 2

import timsort
from color import *
import random
import sorts



# Creates file object
file_obj = open("output_1.txt", "w")


# Creates an array of random integers to use for the average case scenarios
array_average = [random.randint(1, 100000) for _ in range(1000000)]


# Creates arrays of various orders to use for best-case scenarios
bubble_best = [x for x in range(1, 100000)]
tim_best = [x for x in range(1, 100000)]
merge_best = [x for x in range(1, 100000)]

quick_best = []    # <-------------------------------------------------------------------HERE***


# Creates an array of various orders to use for worst-case scenarios for the different sorting methods
bubble_worst = [random.randint(1,100000) for _ in range(1000000)]
bubble_worst.sort(reverse=True)

tim_worst = [random.randint(1,100000) for _ in range(1000000)]
tim_worst.sort(reverse=True)

merge_worst = [random.randint(1,100000) for _ in range(1000000)]
merge_worst.sort(reverse=True)

quick_worst = [x for x in range(1, 100000)]   # Worst case for quick is a pre-sorted ascending order array





# TIMSORT

tim_100, dt_tim_100 = timsort.timSort(array_average[:100])
tim_1000, dt_tim_1000 = timsort.timSort(array_average[:1000])
tim_10000, dt_tim_10000 = timsort.timSort(array_average[:10000])
tim_100000, dt_tim_100000 = timsort.timSort(array_average[:100000])
tim_1000000, dt_tim_1000000 = timsort.timSort(array_average[:1000000])

# Print average case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"TIM SORT AVERAGE CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_tim_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_tim_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_tim_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_tim_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_tim_1000000:0.6f} ms")


# -----------------------------------> TIM BEST CASE <------------------------------------------------
tim_best_100, dt_tim_best_100 = timsort.timSort(tim_best[:100])
tim_best_1000, dt_tim_best_1000 = timsort.timSort(tim_best[:1000])
tim_best_10000, dt_tim_best_10000 = timsort.timSort(tim_best[:10000])
tim_best_100000, dt_tim_best_100000 = timsort.timSort(tim_best[:100000])
tim_best_1000000, dt_tim_best_1000000 = timsort.timSort(tim_best[:1000000])

# Print besst case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nTIM SORT BEST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_best[:10]}"
               f"\n\t\tLast 10: {tim_best[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {tim_best[:10]}"
               f"\n\t\tLast 10: {tim_best[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_best[:10]}"
               f"\n\t\tLast 10: {tim_best[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_best[:10]}"
               f"\n\t\tLast 10: {tim_best[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_best[:10]}"
               f"\n\t\tLast 10: {tim_best[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_tim_best_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_tim_best_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_tim_best_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_tim_best_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_tim_best_1000000:0.6f} ms")


#-------------------------------------> TIM WORST CASE <----------------------------------------------
tim_worst_100, dt_tim_worst_100 = timsort.timSort(tim_worst[:100])
tim_worst_1000, dt_tim_worst_1000 = timsort.timSort(tim_worst[:1000])
tim_worst_10000, dt_tim_worst_10000 = timsort.timSort(tim_worst[:10000])
tim_worst_100000, dt_tim_worst_100000 = timsort.timSort(tim_worst[:100000])
tim_worst_1000000, dt_tim_worst_1000000 = timsort.timSort(tim_worst[:1000000])


# Print worst case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nTIM SORT WORST CASE:"
               f"\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_worst[:10]}"
               f"\n\t\tLast 10: {tim_worst[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_best_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_best_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {tim_worst[:10]}"
               f"\n\t\tLast 10: {tim_worst[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_worst_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_worst_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_worst[:10]}"
               f"\n\t\tLast 10: {tim_worst[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_worst_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_worst_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_worst[:10]}"
               f"\n\t\tLast 10: {tim_worst[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_worst_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_worst_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {tim_worst[:10]}"
               f"\n\t\tLast 10: {tim_worst[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {tim_worst_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {tim_worst_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_tim_worst_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_tim_worst_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_tim_worst_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_tim_worst_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_tim_worst_1000000:0.6f} ms")




# BUBBLESORT

# ------------------------------------> BUBBLE AVERAGE CASE <-----------------------------------------
bubble_100, dt_bubble_100 = sorts.bubbleSort(array_average[:100])
bubble_1000, dt_bubble_1000 = sorts.bubbleSort(array_average[:1000])
bubble_10000, dt_bubble_10000 = sorts.bubbleSort(array_average[:10000])




# Print average case for bubble on 100, 1000, & 10,000 integers
file_obj.write(f"\n\n\n\nBUBBLE SORT AVERAGE CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_10000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_bubble_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_bubble_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_bubble_10000:0.6f} ms")



#---------------------------------> BUBBLE BEST CASE <-----------------------------------------
bubble_best_100, dt_bubble_best_100 = sorts.bubbleSort(bubble_best[:100])
bubble_best_1000, dt_bubble_best_1000 = sorts.bubbleSort(bubble_best[:1000])
bubble_best_10000, dt_bubble_best_10000 = sorts.bubbleSort(bubble_best[:10000])


# Print best case for bubble on 100, 1000, & 10,000 integers
file_obj.write(f"\n\n\n\nBUBBLE SORT BEST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {bubble_best[:10]}"
               f"\n\t\tLast 10: {bubble_best[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_best_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_best_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {bubble_best[:10]}"
               f"\n\t\tLast 10: {bubble_best[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_best_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_best_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {bubble_best[:10]}"
               f"\n\t\tLast 10: {bubble_best[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_best_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_best_10000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_bubble_best_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_bubble_best_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_bubble_best_10000:0.6f} ms")



#--------------------------------> BUBBLE WORST CASE <-------------------------------------------
bubble_worst_100, dt_bubble_worst_100 = sorts.bubbleSort(bubble_worst[:100])
bubble_worst_1000, dt_bubble_worst_1000 = sorts.bubbleSort(bubble_worst[:1000])
bubble_worst_10000, dt_bubble_worst_10000 = sorts.bubbleSort(bubble_worst[:10000])


# Print best case for bubble on 100, 1000, & 10,000 integers
file_obj.write(f"\n\n\n\nBUBBLE SORT WORST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {bubble_worst[:10]}"
               f"\n\t\tLast 10: {bubble_worst[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_worst_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_worst_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {bubble_worst[:10]}"
               f"\n\t\tLast 10: {bubble_worst[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_worst_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_worst_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {bubble_worst[:10]}"
               f"\n\t\tLast 10: {bubble_worst[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {bubble_worst_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {bubble_worst_10000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_bubble_worst_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_bubble_worst_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_bubble_worst_10000:0.6f} ms")




# QUICKSORT

# ---------------------------------> AVERAGE CASE QUICK <----------------------------------------

array_length = len(array_average[:100]) - 1

quick_100, dt_quick_100 = sorts.quick_sort(array_average[:100], 0, array_length)
quick_1000, dt_quick_1000 = sorts.quick_sort(array_average[:1000], 0, array_length)
quick_10000, dt_quick_10000 = sorts.quick_sort(array_average[:10000], 0, array_length)
quick_100000, dt_quick_100000 = sorts.quick_sort(array_average[:100000], 0, array_length)
quick_1000000, dt_quick_1000000 = sorts.quick_sort(array_average[:1000000], 0, array_length)


# Print average case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nQUICK SORT AVERAGE CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_quick_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_quick_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_quick_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_quick_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_quick_1000000:0.6f} ms")


# ------------------------------------> QUICK BEST CASE <--------------------------------------







# -----------------------------------> WORST CASE QUICK <-------------------------------------
array_length = len(quick_worst[:100]) - 1

quick_worst_100, dt_quick_worst_100 = sorts.quick_sort(quick_worst[:100], 0, array_length)
quick_worst_1000, dt_quick_worst_1000 = sorts.quick_sort(quick_worst[:1000], 0, array_length)
quick_worst_10000, dt_quick_worst_10000 = sorts.quick_sort(quick_worst[:10000], 0, array_length)
quick_worst_100000, dt_quick_worst_100000 = sorts.quick_sort(quick_worst[:100000], 0, array_length)
quick_worst_1000000, dt_quick_worst_1000000 = sorts.quick_sort(quick_worst[:1000000], 0, array_length)


# Print best case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nQUICK SORT BEST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {quick_worst[:10]}"
               f"\n\t\tLast 10: {quick_worst[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_worst_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_worst_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {quick_worst[:10]}"
               f"\n\t\tLast 10: {quick_worst[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_worst_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_worst_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {quick_worst[:10]}"
               f"\n\t\tLast 10: {quick_worst[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_worst_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_worst_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {quick_worst[:10]}"
               f"\n\t\tLast 10: {quick_worst[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_worst_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_worst_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {quick_worst[:10]}"
               f"\n\t\tLast 10: {quick_worst[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {quick_worst_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {quick_worst_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_quick_worst_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_quick_worst_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_quick_worst_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_quick_worst_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_quick_worst_1000000:0.6f} ms")














# MERGESORT

# ------------------------------------> MERGE AVERAGE CASE <--------------------------------------

merge_100, dt_merge_100 = sorts.mergeSort(array_average[:100])
merge_1000, dt_merge_1000 = sorts.mergeSort(array_average[:1000])
merge_10000, dt_merge_10000 = sorts.mergeSort(array_average[:10000])
merge_100000, dt_merge_100000 = sorts.mergeSort(array_average[:100000])
merge_1000000, dt_merge_1000000 = sorts.mergeSort(array_average[:1000000])


# Print average case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nMERGE SORT AVERAGE CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {array_average[:10]}"
               f"\n\t\tLast 10: {array_average[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_merge_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_merge_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_merge_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_merge_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_merge_1000000:0.6f} ms")


# ---------------------------------------> BEST MERGE CASE <------------------------------------
merge_best_100, dt_merge_best_100 = sorts.mergeSort(merge_best[:100])
merge_best_1000, dt_merge_best_1000 = sorts.mergeSort(merge_best[:1000])
merge_best_10000, dt_merge_best_10000 = sorts.mergeSort(merge_best[:10000])
merge_best_100000, dt_merge_best_100000 = sorts.mergeSort(merge_best[:100000])
merge_best_1000000, dt_merge_best_1000000 = sorts.mergeSort(merge_best[:1000000])


# Print best case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nMERGE SORT BEST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_best[:10]}"
               f"\n\t\tLast 10: {merge_best[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_best_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_best_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {merge_best[:10]}"
               f"\n\t\tLast 10: {merge_best[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_best_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_best_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_best[:10]}"
               f"\n\t\tLast 10: {merge_best[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_best_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_best_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_best[:10]}"
               f"\n\t\tLast 10: {merge_best[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_best_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_best_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_best[:10]}"
               f"\n\t\tLast 10: {merge_best[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_best_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_best_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_merge_best_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_merge_best_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_merge_best_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_merge_best_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_merge_best_1000000:0.6f} ms")


# ---------------------------------------> WORST MERGE CASE <------------------------------------
merge_worst_100, dt_merge_worst_100 = sorts.mergeSort(merge_worst[:100])
merge_worst_1000, dt_merge_worst_1000 = sorts.mergeSort(merge_worst[:1000])
merge_worst_10000, dt_merge_worst_10000 = sorts.mergeSort(merge_worst[:10000])
merge_worst_100000, dt_merge_worst_100000 = sorts.mergeSort(merge_worst[:100000])
merge_worst_1000000, dt_merge_worst_1000000 = sorts.mergeSort(merge_worst[:1000000])


# Print worst case for timsort on 100, 1000, 10000, 100000, 1000000 integers
file_obj.write(f"\n\n\nMERGE SORT WORST CASE:"
               "\n"
               f"\n100 Integers"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_worst[:10]}"
               f"\n\t\tLast 10: {merge_worst[91:100]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_worst_100[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_worst_100[-10:]}"
               "\n"
               "\n1000 Integers"
               f"\n\tUnsorted:"
               f"\n\t\tFirst 10: {merge_worst[:10]}"
               f"\n\t\tLast 10: {merge_worst[991:1000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_worst_1000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_worst_1000[-10:]}"
               "\n"
               f"\n10000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_worst[:10]}"
               f"\n\t\tLast 10: {merge_worst[9991:10000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_worst_10000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_worst_10000[-10:]}"
               f"\n"
               f"\n100000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_worst[:10]}"
               f"\n\t\tLast 10: {merge_worst[99991:100000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_worst_100000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_worst_100000[-10:]}"
               f"\n"
               f"\n1000000 Integers:"
               f"\n\tUnsorted: "
               f"\n\t\tFirst 10: {merge_worst[:10]}"
               f"\n\t\tLast 10: {merge_worst[999991:1000000]}"
               f"\n\tSorted:"
               f"\n\t\tFirst 10 integers sorted: {merge_worst_1000000[:10]}"
               f"\n\t\tLast 10 integers sorted: {merge_worst_1000000[-10:]}")


file_obj.write(f"\n\n   SORT TIME: "
            f"\n\tTime elapsed for 100 integers: {dt_merge_worst_100:0.6f} ms "
            f"\n\tTime elapsed for 1000 integers: {dt_merge_worst_1000:0.6f} ms"
            f"\n\tTime elapsed for 10000 integers: {dt_merge_worst_10000:0.6f} ms"
            f"\n\tTime elapsed for 100000 integers: {dt_merge_worst_100000:0.6f} ms"
            f"\n\tTime elapsed for 1000000 integers: {dt_merge_worst_1000000:0.6f} ms")
