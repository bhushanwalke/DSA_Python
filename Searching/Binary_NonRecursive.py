def binary_search(items_list, item):
    first = 0
    last = len(items_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last)/2
        if items_list[mid] == item:
            found = True
        else:
            if item < items_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

        return found


print binary_search([1,2,3,4,5,6,7], 4)
print binary_search([1,2,3,4,5,6,7], 0)