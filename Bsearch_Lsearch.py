import time
import random

# Sorts an array from least to greatest
def sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        sort(left)
        sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = right[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

# Searches an array for a specified value using the linear search algorithm
def linear_search(alist, item):
    for i in range(0,len(alist)):
        if alist[i] == item:
            return i

# Searches an array for a specified value using the binary search algorithm
def binary_search(alist, item):
    #sort(alist)
    low = 0
    high = len(alist)

    while low <= high:
        mid = low + (high - low)//2
        if alist[mid] == item:
            return mid

        elif alist[mid] < item:
            low = mid + 1

        else:
            high = mid - 1


# Creates a list of size n with randomized odd values
def create_list(alist, n):
    
    for i in range(0, n):
        rand_even = random.randrange(1,n+1,2)
        alist.append(rand_even)

# Creates a list of size 'size' or appends a random value to 'alist' depending
# on if 'alist' has an even or odd length
def create_target_list(alist, size, size_of_blist, blist):
    # Checks if length of 'alist' is odd and greater than 10
    if size > 10 and (size % 2) != 0:
        rand = random.randrange(11,size_of_blist,2)
        alist.append(rand)
    # Checks if length of 'alist' is even and greater than 10
    elif size > 10 and (size % 2) == 0:
        rand = random.randrange(10, size_of_blist, 2)
        alist.append(rand)

    #Creates 'alist'
    else:
        for x in range(0,size):
            # Appends random values to 'alist' that are not in blist
            if x < size/2:
                rand = random.randrange(10,size_of_blist,2)
            # Appends random values to 'alist' that are in in blist
            if x >= size/2:
                rand = random.randrange(size+1,size_of_blist,2)
                while rand not in blist:
                    rand = random.randrange(size+1,size_of_blist,2)
            alist.append(rand)

# Finds the length of 'target' where binary search is faster
# than linear search
def main(size_of_list):
    k = 10
    alist = []
    blist = []
    target = []
    create_list(alist,size_of_list)
    blist = alist
    # Runs until 'bin_time' < 'lin_time' or hits range max
    for i in range(0, size_of_list):
        create_target_list(target, k, size_of_list, alist)
        # Checks how long linear search takes to check each element
        # in target list
        lin_start = time.time()
        for val in target:
            linear_search(alist, k)
        lin_time = time.time() - lin_start

        # Checks how long binary search takes to check each element
        # in target list
        bin_start = time.time()
        sort(blist)
        for val in target:
            binary_search(blist, k)
        bin_time = time.time() - bin_start

        #Checks if binary search time is less than linear search time
        if bin_time < lin_time:
            print ("Binary search is faster than linear search at k =", str(k))
            break
        # Increases size of target list
        k += 1

# Test code
if __name__ == '__main__':
    main(1000)
    main(5000)
    main(10000)
