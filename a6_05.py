d1 = {}
print("Enter the details for the dictionary:")
n1 = int(input("Enter the number of data in the dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

    
items = list(d1.items())
n = len(items)
for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] > items[j+1][1]:  
            items[j], items[j+1] = items[j+1], items[j]
d2 = dict(items)
print(d2)
