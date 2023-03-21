def function_name_print(a,b,c,d):
    print(a, b, c, d)

def funargs(normal, *args, **kwargs):
    # print(type(args))
    # print(args[0])
    print(normal)
    for item in args:
        print(item)
    print("Roles of some studets: ")
    for key,value in kwargs.items():
        print(f"{key} has a work in {value}")

function_name_print("xyz","abc","pqr","mnp")

lst = ["xyz","abc","pqr","mnp"]
kw = {"abc":"python", "xyz":"java",  "pqr":"javascript",}
normal = "normal argument and students are:"
funargs(normal,*lst,**kw)
