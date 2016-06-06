__author__ = 'bhushan'

def quick_sort(items_list):
    quick_sort_helper(items_list, 0, len(items_list) - 1)

def quick_sort_helper(items_list, first, last):
    if first < last:
        splitpoint = partition(items_list, first, last)

        quick_sort_helper(items_list, first, splitpoint-1)
        quick_sort_helper(items_list, splitpoint+1, last)

def partition(items_list, first, last):
    print "list now ", items_list[first:last]
    pivot = items_list[last]
    pindex = first

    for i in range(last-1):
        if items_list[i] <= pivot:
            items_list[i], items_list[pindex] = items_list[pindex], items_list[i]
            pindex +=1

    items_list[pindex], items_list[last] = items_list[last], items_list[pindex]
    return pindex

items_list = [5,4,3,2,1]
quick_sort(items_list)
print items_list

