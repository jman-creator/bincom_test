import random

binary = ""

for i in range(4):
    binary += str(random.randint(0, 1))

print("Binary: ", binary)

base10 = int(binary, 2)
print("Base10: ", base10)