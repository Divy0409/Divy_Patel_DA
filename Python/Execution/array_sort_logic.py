l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)

new_list = []

while l:
    minimum = l[0]  # method 2
    for x in l: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    l.remove(minimum)    

print (new_list)

max_list = []

while new_list:
    maximum = new_list[0]  # reverse sorting
    for x in new_list: 
        if x > maximum:
            maximum = x
    max_list.append(maximum)
    new_list.remove(maximum)    

print (max_list)