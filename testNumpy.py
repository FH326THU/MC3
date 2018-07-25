import numpy, math, random, time

timeNow = time.time()
for i in range(9999999):
    t = math.atan(random.random())

print("math.atan:" + str(time.time() - timeNow))

timeNow = time.time()
for i in range(9999999):
    t = numpy.arctan(random.random())

print("numpy.arctan:" + str(time.time() - timeNow))