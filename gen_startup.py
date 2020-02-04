import random

companies = open('companies.txt', 'r').readlines()
nouns = open('nouns.txt', 'r').readlines()
verbs = open('verbs.txt', 'r').readlines()

xs = companies + verbs
ys = nouns + verbs

x = xs[int(random.uniform(0, len(xs)))]
y = ys[int(random.uniform(0, len(ys)))]

while y == x:
    y = ys[int(random.uniform(0, len(ys)))]

print("It's {x} for {y}.".format(x=x.strip(), y=y.strip()))
