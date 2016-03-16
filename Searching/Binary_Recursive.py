def binary_recursive(items_list, item):
    if len(items_list) == 0:
        return False
    else:
        mid = len(items_list) / 2
        if items_list[mid] == item:
            return True
        else:
            if items_list[mid] > item:
                return binary_recursive(items_list[:mid], item)
            else:
                return binary_recursive(items_list[mid +1 :], item)


print binary_recursive([1,2,3,4,5,6,7], 4)
print binary_recursive([1,2,3,4,5,6,7], 2)