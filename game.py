import random, time

t = time.time()
random.seed()

re = 0

for x in range(1,11):
  a = random.randint(1, 10)
  b = random.randint(1, 10)
  s = random.choice(["+","-","*"])
  r = int(input("{0}) {1} {2} {3} = \n".format(x, a, s, b)))
  c = eval("a{0}b".format(s))
  if r == c:
    re += 1
  

t1 = time.time()
tem = t1 - t

print("risposte esatte: {0} in {1:.2f}".format(re, tem))
