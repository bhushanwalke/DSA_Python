__author__ = 'bhushan'

def quick_sort(items_list):
    quick_sort_helper(items_list, 0, len(items_list) - 1)

def quick_sort_helper(items_list, first, last):
    if first < last:
        splitpoint = partition(items_list, first, last)

        quick_sort_helper(items_list, first, splitpoint-1)