#Numeric
a = 15
b = 12

sum = a + b
diff = a - b
prod = a * b
div = a / b

print('Sum:', sum, 'difference:', diff, 'prod:', prod, 'division:', div)

c = 4 + 5j
print(c.real, c.imag)


#strings

greeting = 'Hello'
name = 'Alice'

greeting_alice = greeting + ', ' + name
print(greeting_alice)
print(len(greeting_alice))
print(greeting_alice.upper())


#list/tuple

lista = [1, 2, 3, 4, 5]
lista2 = tuple(lista)

lista[2] = 35

print(lista2)

print(lista[1], lista[-1])
print(lista[1:-1])

# SET

setlist =  {1, 2, 2, 3, 3, 3}
print(setlist)
setlist.add(4)
print(setlist)
setlist.remove(3)
print(setlist)

# Dictionary

cliente1 = {
    'name': 'Alice',
    'age' : 20,
    'balance': 55,
}

print(cliente1.get('name'))

cliente1['balance'] = cliente1['balance'] + 100
print(cliente1.get('balance'))

cliente1['status'] = 'value' 
print(cliente1)

# Boolean

x = 10
y = 20

print(x > y)
print(x < y)
print((x > y) and (x < y))
print((x > y) or (x < y))

#NoneType

z =None
print(z is None)

lista5 = [25, 'Boris', True]

print(type(lista5[0]))
print(type(lista5[1]))
print(type(lista5[2]))