input_list=[2,4,6,7,8]
max_value=max(input_list)
min_value=min(input_list)

list2=[]
for i in range(min_value,max_value+1):
    list2.append(i)

set1=set(input_list)
set2=set(list2)
# print(set1)
# print(set2)
missing_num=set2.difference(set1)
missing_num=list(missing_num)
print(missing_num)

