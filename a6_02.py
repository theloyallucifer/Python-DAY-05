n = input("Enter a string: ")
c = {}
for char in n:
    if char in c:
        c[char] += 1
    else:
        c[char] = 1
print(c)
