n = int(input("Enter the number of elements :"))
mylist = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    mylist.append(element)

print("List : ", mylist)

mylist.sort(reverse=True)
if len(mylist) < 3:
    print("List must have at least 3 elements : ")
else:
    print("Third largest digit: ", mylist[2])

length = len(mylist)
print("Length of the list is", length)

mylist.sort()
print("The sorted list is : ", mylist)
