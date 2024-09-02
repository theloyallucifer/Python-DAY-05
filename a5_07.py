n= input("Enter a sequence of comma-separated numbers: ")

numStr = n.split(',')

for i in range(len(numStr)):
    numStr[i] = numStr[i].strip()

numbers = []
for num in numStr:
        numbers.append(int(num))
else:
    result_tuple = tuple(numbers)
    print("The created tuple is:", result_tuple)
