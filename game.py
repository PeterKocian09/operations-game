import random, time

t = time.time()
random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)

c = a + b


for x in range(1,11):
  r = input("%s) %s + %s = \n" % (x, a , b))
  a = random.randint(1, 10)
  b = random.randint(1, 10)

t1 = time.time()
tem = t1 - t

re = 0

if r == c:
  re += 1

print("risposte esatte: %s in %s" %(re, tem))


