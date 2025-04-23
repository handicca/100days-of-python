# Read file
# file = open("./hello.txt")
# print(file.read())
# file.close()
##############
"""
with open("./hello.txt", "r") as file:
    content = file.read()

print(content)
"""

# Write file
with open("./hello.txt", "a") as file:
    file.write("\nMales ngoding ah udah ada AI")