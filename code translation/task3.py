# Create sample employee data
data = {
    "name": ["Anu", "Rahul", "Priya", "Kiran", "Arjun"],
    "salary": [45000, 60000, 75000, 40000, 55000]
}

# Filter employees without relying on an unavailable pandas installation
result = [
    (name, salary)
    for name, salary in zip(data["name"], data["salary"])
    if salary > 50000
]

print("Employees with salary greater than 50000:")
for name, salary in result:
    print(f"{name}  {salary}")