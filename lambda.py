__author__ = 'bhushan'

list1 = [[1,2,3], [2,4,3], [2,3,1], [7,4,8]]
list2 = [4,3,2,5,1,7]

list2.sort()
print(list2)

list1.sort(key=lambda x: x[1])
print(list1)

asd = lambda a,b: a+b

print(asd(5,4))

key = lambda x: x[1]

for i in list1:
    print(key(i))