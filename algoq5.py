array1 = []
array2 = []

count1 = 1
size_1 = int(input("enter the size of the array 1: "))

while count1 <= size_1:
    elementa1 = int(input("enter the element you need to add: "))
    array1.append(elementa1)
    count1 = count1 + 1

print("now add elements to array 2")
count2 = 1
size_2 = int(input("enter the size of the array 2: "))

while count2 <= size_2:
    elementa2 = int(input("enter the element you need to add: "))
    array2.append(elementa2)
    count2 = count2 + 1

print("new array is ", array1+array2)
