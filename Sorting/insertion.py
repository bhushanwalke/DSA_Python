__author__ = 'bhushan'

def insertion(items_list):
    for index in range(1,len(items_list)):
        currentValue = items_list[index]
        position = index

        while position > 0 and items_list[position-1] > items_list[position]:
            items_list[position] = items_list[position-1]
            items_list[position-1] = currentValue


items_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#items_list = [1,2,3,4,5,6,7]
insertion(items_list)
print items_list