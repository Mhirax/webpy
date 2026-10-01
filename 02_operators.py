# Operators in Python

a = 10
b = 3

# Arithmetic — mostly the same as JavaScript, with two extras
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # always a float: 3.3333333333333335
print(a // b)  # floor division: 3  (JS needs Math.floor(a / b))
print(a % b)   # remainder: 1
print(a ** b)  # exponent: 1000  (JS: a ** b too)

# Comparison — these return True / False, capitalised
print(a > b, a < b, a == b, a != b)

# There is no === in Python. == compares values:
print(1 == 1.0)  # True — different types, same value

# `is` compares identity (same object in memory), NOT value.
# Use it only for None, True, False — never for numbers or strings.
x = None
print(x is None)

# Logical operators are words, not symbols
print(True and False)  # &&
print(True or False)   # ||
print(not True)        # !

# `in` checks membership — handy and has no direct JS operator
print("py" in "python")
print(3 in [1, 2, 3])

# Augmented assignment works like JS, but there is no ++ or --
count = 0
count += 1
print(count)
