import math

area = 70368744177664
side = area**(0.5)
print("Iteration 1:")
print("Side: {}".format(side))
print("Area: {}\n".format(area))

for i in range(24):
    side = (side) / (2*math.cos(45))
    area = area + (2*(side**2))
    print("Iteration {}".format(i+2))
    print("Side: {}".format(side))
    print("Area: {}\n".format(area))

print("Total Area at 25 = {}".format(area))
print(area)

