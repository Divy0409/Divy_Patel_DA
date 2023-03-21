def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  
# If poor and not both present in string it will be replaced by the word good...
  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
print(not_poor('This is not poor!'))
print(not_poor('This is not good!'))
