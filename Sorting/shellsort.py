__author__ = 'bhushan'


def shellSort(items_list):
    sublist = len(items_list)/2

    while sublist > 0:
        for start_pos in range(sublist):
            gap_insertionSort(items_list, start_pos, sublist)

        print(sublist, "", items_list)

        sublist = sublist/2

def gap_insertionSort(items_list, start, gap):
    for i in range(start + gap, len(items_list), gap):
        current_value = items_list[i]
        position = i

        while position >= gap and items_list[position-gap] > current_value:
            items_list[position] = items_list[position-gap]
            items_list[position-gap] = current_value
            position = position-gap


items_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(items_list)
print items_list