from timeit import default_timer as time

def heapify_max(lst, heap_size, i):
    largest = i
    swaps_counter = 0
    comparisons_counter = 0

    l, r = i*2+1, i*2+2

    if l < heap_size and lst[l] > lst[largest]:
        largest = l
    comparisons_counter += 2

    if r < heap_size and lst[r] > lst[largest]:
        largest = r
    comparisons_counter += 2

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_max(lst, heap_size, largest)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment

    return swaps_counter, comparisons_counter

def heapify_min(lst, heap_size, i):
    least = i
    swaps_counter = 0
    comparisons_counter = 0

    l, r = i*2+1, i*2+2

    if l < heap_size and lst[l] < lst[least]:
        least = l
    comparisons_counter += 2

    if r < heap_size and lst[r] < lst[least]:
        least = r
    comparisons_counter += 2

    if least != i:
        lst[i], lst[least] = lst[least], lst[i]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_min(lst, heap_size, least)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment

    return swaps_counter, comparisons_counter

def heap_sort(lst, sort_order = "asc"):
    start_time = time()
    swaps_counter = 0
    comparisons_counter = 0

    if sort_order == "asc":
        for j in range((len(lst)-2)//2, -1, -1): 
            swaps_counter_increment, comparisons_counter_increment = heapify_max(lst, len(lst), j)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment
            
        for end in range(len(lst)-1, 0, -1): 
            
            lst[end], lst[0] = lst[0], lst[end] 
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_max(lst, end, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment
    
    elif sort_order == "desc":
        for j in range((len(lst)-2)//2, -1, -1):
            swaps_counter_increment, comparisons_counter_increment = heapify_min(lst, len(lst), j)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

        for end in range(len(lst)-1, 0, -1):
            lst[end], lst[0] = lst[0], lst[end] 
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_min(lst, end, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

    else:
        print("Wrong sort order")
        return

    execution_time = (float(time() - start_time))*1000
    print("------------------------------------------")
    print("Heap Sort:")
    print("Execution time:", execution_time, "ms")
    print("Comparisons:", comparisons_counter)
    print("Swaps:", swaps_counter)
    print(lst)
    print("------------------------------------------")

    return lst
