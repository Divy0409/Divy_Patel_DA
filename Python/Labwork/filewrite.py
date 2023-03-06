# f = open("file2.txt","w")
# f.write("c is one of the oldest programming languages\n")

# f = open("file2.txt","a")
# a = f.write("c is one of the oldest programming languages\n")
# print(a)

#f.close()

# Handle read and write both
f = open("file2.txt","r+")
print(f.read())
f.write("thank you")
