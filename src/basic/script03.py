import math
import random

print(math.pi)
print(math.sqrt(2))

print(random.random())
print(random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))

s = 'spam'
print(len(s))

l = 'ohayo kosaimusu'
l1 = l.split(' ') 
print(l1)

print('%s is %s' %('cat' , 'animal'))
print('{} is {}' .format('dog' , 'animal'))

f = open('data.txt' , 'w')
f.write('OHAYO')
f.close()