__author__ = 'bhushan'

def merge_sort(items_list):
    print "splitting list", items_list
    if len(items_list) > 1:
        mid = len(items_list) / 2
        left_half = items_list[:mid]
        right_half = items_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        j = 0
        i = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                items_list[k] = left_half[i]
                i = i + 1
            else:
                items_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            items_list[k] = left_half[i]
            i = i +1
            k = k+1

        while j <len(right_half):
            items_list[k] = right_half[j]
            j = j+1
            k = k+1

    print "merging list", items_list


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)