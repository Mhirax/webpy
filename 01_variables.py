# Variables in Python
# No `let`, `const` or `var` keyword — you just name it and assign it.

name = "Mhirax"
age = 25
height = 5.9
is_learning = True

# print() is Python's console.log()
print(name)
print(age)
print(height)
print(is_learning)

# print() takes multiple arguments and joins them with a space
print("Name:", name, "| Age:", age)

# f-strings are template literals: f"..." instead of `...`
print(f"{name} is {age} years old and {height}ft tall.")

# type() tells you what a value is — like typeof in JavaScript
print(type(name), type(age), type(height), type(is_learning))
