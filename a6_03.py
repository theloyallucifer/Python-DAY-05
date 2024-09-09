name = input("Enter employee names separated by commas: ").split(',')
salary = input("Enter corresponding salaries separated by commas: ").split(',')
d= {}

for i in range(len(name)):
    ename = name[i].strip()
    esalary = int(salary[i].strip())
    d[ename] = esalary

print(d)
