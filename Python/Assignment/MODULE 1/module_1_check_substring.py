test_list = [5, 6, 3, 8, 2, 1, 7, 1]
 
print("The original list : " + str(test_list))

sublist = [8, 2, 1]

# To check wether same item is present at any index in sublist
res = any(test_list[idx: idx + len(sublist)] == sublist
          for idx in range(len(test_list) - len(sublist) + 1))
 

print("Is sublist present in list ? : " + str(res))