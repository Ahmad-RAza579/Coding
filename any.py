with open("file.txt","w") as file:
    file.write("i am doing coding")
file.close()
with open("file.txt","r") as file:
    data = file.readlines()
    for i in data:
        word = i.split()
        print(word)
file.close