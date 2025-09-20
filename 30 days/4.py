# Day 4

print(" ".join(['Thirty', 'Days', 'Of', 'Python']))

print(" ".join(['Coding', 'For', 'All']))

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print("Coding" in company)

print(company.replace("Coding", "Python"))

print(company.replace("Coding For All", "Python for Everyone"))

print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

print(company[0])
print(company[-1])
print(company[10]) #space

P4E = "Python For Everyone"
print(P4E)
C4A = "Coding For All"
print(C4A)

print(company.index("C"))
print(company.index("F"))
print(company.rfind("I"))

bec = "You cannot end a sentence with because because because is a conjunction"
print(bec.find("because"))
print(bec.rindex("because"))

print(bec[:31] + bec[55:])

print(company.startswith("Coding For All"))
print(company.endswith("Coding For All"))

remove_spaces = '   Coding For All      '
print(remove_spaces.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(python_libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with radius {radius} is {area} meters square.")

a = 8
b = 6
print(f"8 + 6 = {a + b}")
print(f"8 - 6 = {a - b}")
print(f"8 * 6 = {a * b}")
print(f"8 / 6 = {(a / b):.2f}")
print(f"8 % 6 = {a % b}")
print(f"8 // 6 = {a // b}")
print(f"8 ** 6 = {a ** b}")
