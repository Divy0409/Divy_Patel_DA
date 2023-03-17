"""
*args = arguments (tuple in parameter)
**kargs = key with arguments (dictionary as parameter)

"""
# normal function with normal parameter

def sum(n1,n2):
    ans  = n1 + n2
    print(ans)
sum(10,20)

# args function 
def addition(*n):
    ans = 0
    for i in n:
        ans += i
    print(ans)

addition(10,20,30,40,50)

def myfun(**kargs):
    for k,v in kargs.items():
        print(f"{k} = {v}")

myfun(name="abc",subject="python")