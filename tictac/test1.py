import random

a = str(random.randrange(10, 99, 1))

unit = ('x', 'y', 'o', 'w', 'e', 'h')
u = random.choice(unit)

print(f"{a = }")
print(f"{u = }")


