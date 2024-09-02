n = input("Enter a sequence of comma-separated numbers: ")

numStr = n.split(',')
for i in range(len(numStr)):
    numStr[i] = numStr[i].strip()

numTup = ()
for num in numStr:
        numTup += (int(num),)
else:
    total_sum = 0
    for number in numTup:
        total_sum += number

    print("The sum of the elements in the tuple is:", total_sum)
