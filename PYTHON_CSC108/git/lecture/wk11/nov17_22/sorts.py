def bubble_sort(L):
    '''(list) -> None
    
    Sort the items in L in non-descending order.
    '''
    
    for iteration in range(len(L)):
        for index in range(len(L) - 1 - iteration):
            if L[index] > L[index + 1]:
                L[index], L[index + 1] = L[index + 1], L[index]

# =========================================================
        
# The core of the insertion_sort algorithm is the "insert" operation. This function
# inserts the next item in the "unsorted" part of the list into the correct place
# in the sorted section of the list.
def insert(L, index):
    '''(list, int) -> None
    
    Insert the item at position index in list L into the range [0..index] so
    that [0..index] is in sorted order. [0..index-1] is already sorted.
    '''
    
    while index > 0 and L[index - 1] > L[index]:
        L[index], L[index - 1] = L[index - 1], L[index]
        index -= 1

def insertion_sort(L):
    '''(list) -> None
    
    Sort the items in L in non-descending order.
    '''
    
    print(L)
    for index in range(len(L)):
        insert(L, index)
        print(L)
        
# =========================================================
  
# The core of the selection sort algorithm is the "find minimum" operation. This
# finds the next item to be placed into the sorted section of the list.
def find_min(L, index):
    '''(list, int) -> int
    
    Return the index of the smallest number in list L that is at or after
    position index.
    '''

    # Useful trick: When you need to find the smallest (or largest) item in a list,
    # set the initial value to the first item in the list.
    smallest_index = index
    for i in range(index, len(L)):
        if L[smallest_index] > L[i]:
            smallest_index = i
    return smallest_index
                
def selection_sort(L):
    '''(list) -> None
    
    Sort the items in L in non-descending order.
    '''
    
    for index in range(len(L)):
        swap_index = find_min(L, index)
        L[index], L[swap_index] = L[swap_index], L[index]

# ========================================================

def mergesort(L):
    '''(list) -> list
    
    Return a list that contains the items in L in non-descending order.
    '''
    
    # Recursive algorithm: base case. 
    if len(L) < 2:
        return L

    # Recursive case. Note how the problem gets smaller (sorting a smaller 
    # list) on each call.  
    midpt = len(L) // 2
    L1 = mergesort(L[: midpt])
    L2 = mergesort(L[midpt: ])
    merged = merge(L1, L2)
    return merged

def merge(L1, L2):
    '''(list, list) -> list
    
    Return a new list that contains the items in L1 and L2 in 
    non-descending order. L1 and L2 are both already in that order.
    '''
    
    merged = []
    index1, index2 = 0, 0
    # merge the two lists until one is empty
    while index1 < len(L1) and index2 < len(L2):
        if L1[index1] < L2[index2]:
            merged.append(L1[index1])
            index1 += 1
        else:
            merged.append(L2[index2])
            index2 += 1

    # If a list is empty, it doesn't change the accumulated list if we add it.    
    merged += L1[index1:]
    merged += L2[index2:]
    return merged

# ========================================================
 
def system_sort(L):
    '''(list) -> None
    
    Sort the items in L in non-descending order.
    '''
    L.sort()
        
if __name__ == "__main__":
    from timing import time_listfunc

    for sz in range(1000, 8001, 1000):
        print("Bubble Sort on %d items: %f" % (sz, time_listfunc(bubble_sort, sz, 1)))
        print("Selection Sort on %d items: %f" % (sz, time_listfunc(selection_sort, sz, 3)))
        print("Insertion Sort on %d items: %f" % (sz, time_listfunc(insertion_sort, sz, 3)))
        print("Merge Sort on %d items: %f" % (sz, time_listfunc(mergesort, sz, 3)))
        print("System Sort on %d items: %f" % (sz, time_listfunc(system_sort, sz, 3)))