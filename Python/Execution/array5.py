def rot_a(a,n):
    b = len(a)
    a[:]=a[n:b]+a[0:n]
    return a


a = [1,2,3,4,5,6,7,8]
n = int(input("Enter the number of time you want to rotate array: "))
print(rot_a(a,n))


