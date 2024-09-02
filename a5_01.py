length = int(input("Enter the number of elements: "))
my_list = []


for i in range(length):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)

print("The list with 7 elements is:")
print(my_list)

list_max = my_list[0]
list_min = my_list[0]

for i in range(length):
    if my_list[i]>list_max:
        list_max = my_list[i]

for i in range(length):
    if my_list[i]<list_min:
        list_min = my_list[i]

print(f"Maximum element = {list_max} \n Minimum element = {list_min}")