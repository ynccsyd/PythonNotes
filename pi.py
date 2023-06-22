import random

aralik = 1000
a = 0
b = 0

for i in range(aralik**2):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    merkez = rand_x**2 + rand_y**2

    if merkez <= 1:
        a += 1
    else:
        b += 1

pi = 4 * (a / (a + b))
print("Estimated pi:", pi)


reduce(lambda a,b:a*b,[1,2,3],2)