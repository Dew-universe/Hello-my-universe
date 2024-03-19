import sys
import script01

print(sys.platform)
print(3**100)
x = 'spam!'
print( x * 8 )

x = input('input x ')
y = input('input y ')
z = script01.add(int(x),int(y))
print(x,'+',y,'=',z)

input('press enter fot exit')