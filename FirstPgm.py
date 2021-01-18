import random
for i in range(3,8,2):
    print('i = ' +str(i))

for i in range(1,5):
    print('i = ' +str(i))

total = 0
for n in range(101):
    total += n
print('Total(1+..+100) is ' + str(total))

for a in range(5):
    print(random.randint(1,9000))