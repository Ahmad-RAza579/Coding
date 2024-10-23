file=open("file.txt","r")
print("The whole file")
a=file.readlines()
for i in range(1,len(a)+1):
    if i%2!=0:
        print(file.readline())
    else:
        pass 
file.close()
