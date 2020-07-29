# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
#fSet.add('v')
l = True
l2 = l
print(id(l))
print(id(l2))
l = False
print(l)
print(l2)
print(id(l))
print(id(l2))

test = '12'

for n in range(1, 11):
  test += str(n)
  print(test)
  print(id(test))

