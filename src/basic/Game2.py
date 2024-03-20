count = 1
while count <=5:
    print(count)
    count+=1

print('dew')

count = 1
for count in range(1,6):
    print(count)
    
for i in range(1,4):
    print('*'*3)

score = 100
health = 60
damage = 50
fugu = 'tasty'

print(score != 101)
print(health - damage > 0)
print(fugu == 'tasty')
 
if fugu == 'tasty':
   print('eat the fugu!')

price = 60
if fugu == 'tasty' and price < 100:
   print('eat the fugu!')

if fugu == ('poison'):
    print('dont eat it')
else:
    print('eat the fugu!')

if price < 20:
    print ('cheap fugu!')
elif price < 100:
    print ('reasonably price fugu!')
else:
    print('Expensive fugu!!!')

def fugu_tip(price, num_plates, tip):
    total = price * num_plates
    tip = total * (tip/100)
    return tip

print(fugu_tip(100,2,15))
print(fugu_tip(50,1,5))