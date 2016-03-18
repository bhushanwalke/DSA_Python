__author__ = 'bhushan'

def bubble(items_list):
    exchange = True;
    pass_num = len(items_list)-1
    while pass_num > 0 and exchange:
        exchange = False
    #for pass_num in range(len(items_list)-1, 0, -1):
        print "Pass:", pass_num
        for i in range(pass_num):
            if items_list[i] > items_list[i+1]:
                exchange = True
                items_list[i], items_list[i+1] = items_list[i+1], items_list[i]

        pass_num -= 1


items_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#items_list = [1,2,3,4,5,6,7]
bubble(items_list)
print items_list