# http://tinyurl.com/z2m2115

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

multi_list = []

for i in list1 :
    for j in list2 :
        multi = i * j
        multi_list.append(multi)

print(multi_list)
