from singleton import OnlyOne

x = OnlyOne()
x.val = 'sausage'
print(x)

y = OnlyOne()
y.val = 'eggs'
print(y)

z = OnlyOne()
z.val = 'spam'
print(z)

print(x)
print(y)
