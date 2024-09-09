dict1 = {}
dict2 = {}
print("Enter the details for 1st dictionary:")
n1 = int(input("Enter the number of data in 1st dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

print("Enter the details for 2nd dictionary: ")
n2 = int(input("Enter the number of data in 2nd dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
d = {}
for key in dict1:
    d[key] = dict1[key]

for key in dict2:
    d[key] = dict2[key]

print(d)
