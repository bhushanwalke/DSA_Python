import sys
def findmin(num):
    num_list = list(str(num))
    print num_list
    min_num = str(sys.maxint)
    for i in range(1, len(num_list)-2):
        if num_list[i-1] < num_list[i] > num_list[i+1]:
            tmp_org = num_list[0:i+1] + num_list[i+2:len(num_list)]
            tmp_num = ''.join(tmp_org)
            print "tmp_num: ", tmp_num
            min_num = min(min_num, tmp_num)
    return min_num



print findmin(23485647)
