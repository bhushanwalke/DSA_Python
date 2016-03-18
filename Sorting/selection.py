__author__ = 'bhushan'

def selection(items_list):
    for fill_slot in range(len(items_list)-1, 0, -1):
        pos_max = 0
        for loc in range(1, fill_slot+1):
            print pos_max
            if items_list[pos_max] < items_list[loc]:
                pos_max = loc

        items_list[fill_slot], items_list[pos_max] = items_list[pos_max], items_list[fill_slot]


items_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#items_list = [1,2,3,4,5,6,7]
selection(items_list)
print items_list