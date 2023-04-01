# keywords: A word ehich have predefined meaning
    # A reserve word
    # It can not be taken as a variable

"""
for
while
break
continue..
"""

import keyword

keyword_list = keyword.kwlist

# print(keyword_list)

word = input("Enter word:")
if word in keyword_list:
    print("Yes it is a keyword.")
else:
    print("No it is not a keyword.")