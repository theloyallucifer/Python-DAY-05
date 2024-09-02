n1 = int(input("Enter the number of elements in list 1: "))
n2 = int(input("Enter the number of elements in list 2: "))
l1 = []
l2 = []
l3 = []

for i in range(n1):
    element = input(f"Enter element {i + 1} in list 1: ")
    l1.append(element)

print(f"List 1: {l1}")


for i in range(n2):
    element = input(f"Enter element {i + 1} in list 2: ")
    l2.append(element)

print(f"List 2: {l2}")


for i in range(n1):
        l3.append(l1[i])

for i in range(n2):
        l3.append(l2[i])

print(f"Concatenated list is: {l3}")
