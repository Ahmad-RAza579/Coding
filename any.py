def largest_number(i):
    largest = i[0]  
    for num in i:    
        if num > largest:
            largest = num   
    return largest
my_list = [11,54,76,87,98,79,0.9,99,67,900,1049]
a = largest_number(my_list)
print(a)