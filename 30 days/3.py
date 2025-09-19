#Exercise 3

age = 19
height = 176.0
complex = 1j + 3

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
print("Perimeter:", 2 * (length * width))

radius = int(input("Write radius: "))
print("Area:", 3.14 * radius * radius)
print("Circumference:", 2 * 3.14 * radius)

slope = 2
print(f"Slope: {slope}")
print("x-intercept:",(1, 0))
print("y-intercept:",(0, -2))

slope0 = (2 - 10) / (2 - 6)
print(f"Slope0: {slope0}")

print(slope > slope0)
print(slope < slope0)
print(slope == slope0)



