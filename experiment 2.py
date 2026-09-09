
# Control Flow Statement
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# For Loop
print("\nNumbers from 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

# While Loop
print("\nNumbers from 5 to 1 using while loop:")
i = 5
while i >= 1:
    print(i)
    i -= 1

# Break Statement
print("\nDemonstrating break statement:")
for i in range(1, 10):
    if i == 6:
        break
    print(i)

# Continue Statement
print("\nDemonstrating continue statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
