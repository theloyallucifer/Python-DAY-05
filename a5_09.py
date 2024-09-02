n = input("Enter a sequence of comma-separated numbers: ")

numStr = n.split(',')
for i in range(len(numStr)):
    numStr[i] = numStr[i].strip()

numbers_tuple = ()
for num in numStr:
        numbers_tuple += (int(num),)
else:
    total_sum = 0
    count = 0
    
    for number in numbers_tuple:
        total_sum += number
        count += 1
    
    if count > 0:
        mean = total_sum / count
        print("The mean is:", mean)
    else:
        print("Mean can't be calculated.")
