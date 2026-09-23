def empcalc():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    sal = float(input("Enter Salary:"))

    if sal >= 50000:
        category = "High Salary"
    elif sal >= 30000:
        category = "Medium Salary"
    else:
        category = "Low Salary"

    employee = (name, age, sal, category)

    print(employee)

empcalc()
