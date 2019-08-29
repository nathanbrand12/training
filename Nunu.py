x = 0
x = x + 1
print(x)
print('---------------------------------------------------')
n = 5
while n > 0:
    print(n)
    n = n - 1
    print ('Blastoff')
print('-----------------------------------')
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
print('---------------------------------------------------')
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line =='done':
        break
    print(line)
print('Done!')
print('---------------------------------------------------')
friends = ['John', 'Nick', 'Bobby']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
print('---------------------------------------------------')
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print('Count: ', count)
print('---------------------------------------------------')

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
print('---------------------------------------------------')
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
print('---------------------------------------------------')
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest