def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    print(f"Product of all elements: {result}")


n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    lst.append(element)

multiply_list(lst)



