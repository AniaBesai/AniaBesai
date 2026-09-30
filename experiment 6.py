employee={
         "name":"Amit",
         "age":20,
         "salary":50000
}
print("The Dict is",employee)
print("Name of the dict field:", employee["name"])
print("Age of the dict field:", employee["age"])
print("Salary of the dict field", employee["salary"])

employee["salary"]=60000
print("after adding:")
print(employee)
employee["age"]=21
print("after updating")
print(employee)
del employee["salary"]

print("keys:")
print(employee.keys())
print("values:")
print(employee.values())
print("items:")
print(employee.items())

print("name:",employee.get("name"))
print("salary:",employee.get("salary","Not Available"))
employee.update({"age":21, "salary":60000})
print("after update")
print(employee)

text=input("enter a string:")
frequency={}

for ch in text:
    if ch in frequency:
        frequency[ch]=frequency[ch]+1
    else:
        frequency[ch]=1

print("character frequency:")
for ch, count in frequency.items():
    print(ch,":",count)
