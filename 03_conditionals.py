# Conditionals in Python
# No parentheses around the condition, no braces around the body.
# A colon opens the block and INDENTATION defines it — indentation is syntax here,
# not style. Four spaces is the convention.

age = 20

if age >= 18:
    print("Adult")
elif age >= 13:        # `elif`, not `else if`
    print("Teenager")
else:
    print("Child")

# Truthiness: empty things are falsy, filled things are truthy.
# Falsy values: False, None, 0, 0.0, "", [], {}, ()
name = ""
if name:
    print("Has a name")
else:
    print("Name is empty")

items = [1, 2, 3]
if items:
    print(f"{len(items)} items")

# Chained comparison — Python lets you write this the way maths does.
# In JS you would need (score > 50 && score < 100).
score = 75
if 50 < score < 100:
    print("In range")

# Ternary reads as a sentence: <value> if <condition> else <value>
# JS: const status = age >= 18 ? "adult" : "minor"
status = "adult" if age >= 18 else "minor"
print(status)

# None is Python's null. Check it with `is`, not ==
user = None
if user is None:
    print("No user logged in")

# `pass` is a do-nothing placeholder — a block cannot be empty
if score > 1000:
    pass
