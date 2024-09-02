n1 = int(input("Enter the number of elements in list: "))
l1 = []
l2 = []
for i in range(n1):
    element = input(f"Enter element {i + 1} in list: ")
    l1.append(element)

print(f"List: {l1}")

for i in range(n1):
    for j in range(n1):
        p = l1[i] * l1[j]
        row = []
        if p % 2 != 0: 
            row = [l1[i], l1[j]]
    l2.append(row)

print("The pairs are: \n")
for row in l2:
    print(row)