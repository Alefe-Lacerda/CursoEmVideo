a = int(input('Número a: '))
b = int(input('Número b: '))
c = int(input('Número c: '))

if a > b and a > c:
    print('{} é o maior número'.format(a))
elif b > a and b > c:
    print('{} é o maior número'.format(b))
elif c > a and c > b:
    print('{} é o maior número'.format(c))

if a < b and a < c:
    print('{} é o menor número'.format(a))
elif b < a and b < c:
    print('{} é o menor número'.format(b))
elif c < a and c < b:
    print('{} é o menor número'.format(c))

