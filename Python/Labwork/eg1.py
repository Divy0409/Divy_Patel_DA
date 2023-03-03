#
# m=int(input())
# n=input()
# sum=0
# product=1
# for j in n:
#     sum=sum+int(j)
#     product=product*int(j)
# out=product-sum
# print(
n=int(input())
k=1
sum=0
while(k<=n):
        sum=sum+(1/k)
        k=k+1

s = "%.4f" % float(sum)
print(f"Harmonic sum upto {n-1} decimal places:", s)




