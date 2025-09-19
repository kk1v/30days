# Exercise 3

age = 19
height = 176.0
complex1 = 1j + 3

base = int(input("Write base "))
h = int(input("Write height "))
print("The area of the triangle is", int(0.5 * base * h))

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is", int(a + b + c))

length = int(input("Write length: "))
width = int(input("Write width: "))
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

radius = int(input("Write radius: "))
print("Area:", 3.14 * radius * radius)
print("Circumference:", 2 * 3.14 * radius)

slope = 2
print(f"Slope: {slope}")
print("x-intercept:", (1, 0))
print("y-intercept:", (0, -2))

slope0 = (2 - 10) / (2 - 6)
print(f"Slope0: {slope0}")

print(slope > slope0)
print(slope < slope0)
print(slope == slope0)

x = 0
y = x ** 2 + 6 * x + 9
print(f"Y is {y}")

x = 1
y = x ** 2 + 6 * x + 9
print(f"Y is {y}")

x = 2
y = x ** 2 + 6 * x + 9
print(f"Y is {y}")

x = 3
y = x ** 2 + 6 * x + 9
print(f"Y is {y}")


print(len("python") != len("dragon"))

operator = ("on" in "python") and ("on" in "dragon")
print(operator)
operator0 = "jargon" in "I hope this course is not full of jargon"
print(operator0)
operator1 = ("on" not in "python") and ("on" not in "dragon")
print(operator1)

length = len("python")
print(float(length))
print(str(length))

print((7 // 3) == int(2.7))

str1 = type("10")
int1 = type(10)
print(str1 == int1)

print(int(float("9.8")) == 10)

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

years = int(input("Enter number of years you have lived: "))
second = years * 31_536_000
print(f"You have lived for {second} seconds.")

print(1, 1, 1, 1, 1)
print(2, 2 // 2, 2 * 1, 2 * 2, 2 * 2 * 2)
print(3, 3 // 3, 3 * 1, 3 * 3, 3 * 3 * 3)
print(4, 4 // 4, 4 * 1, 4 * 4, 4 * 4 * 4)
print(5, 5 // 5, 5 * 1, 5 * 5, 5 * 5 * 5)
