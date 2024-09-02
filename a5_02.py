rows1 = int(input("Enter the number of rows in matrix 1: "))
cols1 = int(input("Enter the number of columns in matrix 1: "))

rows2 = int(input("Enter the number of rows in matrix 2: "))
cols2 = int(input("Enter the number of columns in matrix 2: "))
    
matrix1 = []
matrix2 = []
    
print("Enter the elements in matrix 1:")
for i in range(rows1):
    row1 = []
    for j in range(cols1):
        element = int(input(f"Enter element for position ({i+1}, {j+1}): "))
        row1.append(element)
    matrix1.append(row1)

print("The matrix 1 is:")
for row1 in matrix1:
    print(row1)



print("Enter the elements in matrix 2:")
for i in range(rows2):
    row2 = []
    for j in range(cols2):
        element = int(input(f"Enter element for position ({i+1}, {j+1}): "))
        row2.append(element)
    matrix2.append(row2)

print("The matrix 2 is:")
for row2 in matrix2:
    print(row2)



# rows_A = len(rows1)
# cols_A = len(cols2[0])
# rows_B = len(rows2)
# cols_B = len(cols2[0])

if cols1 != rows2:
    print("Multiplication is not possible.")

# result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
matrix3 = []

for i in range(rows1):
    sum_product = 0
    row = []
    for j in range(cols2):
        sum_product = 0
        for k in range(cols1):
            sum_product += matrix1[i][k] * matrix2[k][j]
        row.append(sum_product)
    matrix3.append(row)

# Print the result matrix
print("Result of matrix multiplication:")
for rows in matrix3:
    print(rows)