# list1=["Harry","Larry","Carry","Marie"]
# for item in list1:
#     print(item)
#
#
# list2=[["Harry",1],["Larry",2],["Carry",5],["Marie",250]]
# dic1=dict(list2)
# print(dic1)
# for item,cars in dic1.items():
#     print(item,"and cars are",cars)
list=[1,2,3,4,"car","motorbike","aeroplanes",5,6,7,8,"boats"]
for items in list:
    if str(items).isnumeric() and items>=6:
        print(items)
