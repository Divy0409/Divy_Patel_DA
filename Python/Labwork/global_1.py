# l = 10 # global

# def function1(n):
#    # l = 5 # local
#     m = 8 # local
    
#     global l
#     l = l + 95
#     print(l,m)
#     print(n,"I have printed ")

# function1("This is me")
# # print(l)

x = 90
def abc():
    x = 20
    def xyz():
        global x 
        x = 95
    print("Before calling xyz()",x)
    xyz()
    print("After calling xyz()",x)
abc()
print(x)