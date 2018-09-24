import math
print('enter the equation (for example 5+2)')
a, c, b = input().split('\040')
if a != 'e':
    a = int(a)
    b = int(b)
else:
    b = int(b)


if c == '+':
    z = a+b
    print('result', z, end='')
elif c == '-':
    z = a*b
    print('result', z, end='')
elif c == '*':
    z = a*b
    print('result', z, end='')
elif c == '/':
    z = a/b
    print('result', z, end='')
elif c == '/':
    z = a / b
    print('result', z, end='')
elif c == '**' and a != 'e':
    z = a**b
    print('result', z, end='')
elif a == 'e':
    z = math.exp(b)
    print('result', z, end='')




else:
    print('invalid operation')



