def reverseList(list1):
    list2 = []
    while len(list1) > 0:
        print list1
        reverseList(list1[1:len(list1)])

        return list2

print reverseList([1,2,3,4,5])
