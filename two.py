from random import *
from turtle import *

speed(10000)
ht()
x = int(randint(1, 1000))

color('purple', 'cyan')


for i in range(x):
    fd(randint(1, 10))
    lt(randint(-360, 360))
    i += 1


print(x)
done()