# Loops in Python
# Every for loop is a for...of loop. There is no C-style for (i = 0; i < n; i++).

languages = ["python", "javascript", "go"]

# Loop over the items directly
for language in languages:
    print(language)

# range(stop) gives 0..stop-1 — this is how you count
for i in range(3):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# Need the index AND the item? enumerate() gives both.
# JS: languages.forEach((lang, i) => ...)
for index, language in enumerate(languages):
    print(f"{index}: {language}")

# Loop over two lists side by side
versions = [3.12, 2024, 1.23]
for language, version in zip(languages, versions):
    print(language, version)

# while works like JS, minus the parentheses
count = 3
while count > 0:
    print(count)
    count -= 1
print("Liftoff")

# break and continue behave exactly as in JavaScript
for number in range(10):
    if number == 3:
        continue   # skip this one
    if number > 5:
        break      # stop entirely
    print(number)

# A for/while can have an `else` — it runs only if the loop was NOT broken.
# No JS equivalent; useful for search loops.
for language in languages:
    if language == "rust":
        print("Found rust")
        break
else:
    print("rust not in the list")

# Looping over a dict gives you the keys; .items() gives key and value
stack = {"frontend": "react", "backend": "python"}
for layer, tool in stack.items():
    print(layer, "->", tool)
