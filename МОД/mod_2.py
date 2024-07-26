import math
# метод левых прямоугольников
def f(x):
    return math.exp(-x**2)
n = input().split()
# print(n)
def f_pramougolnik(a, b, n):
    sum = 0
    h = (b - a) / n
    for i in range(int(n)):
        xi = a + i * h
        sum += f(xi)
    return h * sum
for i in range(len(n)):
    print(f_pramougolnik(0, 3, int(n[i])))
# метод центральных прямоугольников
def f_centr_pramougolnik(a, b, n):
    sum = 0
    h = (b - a) / n
    for i in range(int(n)):
        xi = a + i * h
        xi_plus = a + (i + 1) * h
        sum += f((xi + xi_plus)/2)
    return h * sum
for i in range(len(n)):
    print(f_centr_pramougolnik(0, 3, int(n[i])))
# метод трапеций
def f_trapeci(a, b, n):
    sum = 0
    h = (b - a) / n
    for i in range(int(n)):
        xi = a + i * h
        if i == 0 or i == n - 1:
            sum += f(xi) / 2
        else:
            sum += f(xi)
    return h * sum
for i in range(len(n)):
    print(f_trapeci(0, 3, int(n[i])))
# формула Симпсона
def f_simpson(a, b, n):
    sum = 0
    h = (b - a) / n
    for i in range(int(n)):
        xi = a + i * h
        if i == 0 or i == n - 1:
            sum += f(xi)
        elif i % 2 == 1:
            sum += 4 * f(xi)
        else:
            sum += 2 * f(xi)
    return h / 3 * sum
for i in range(len(n)):
    print(f_simpson(0, 3, int(n[i])))
# уточнение по ричордсону
# for i in range(len(n)):
#     print(f_centr_pramougolnik(0, 3, int(n[i])/4), end='---')
#     print(f_centr_pramougolnik(0, 3, int(n[i])/2), end='+++')
def richordson(a, b, n, operation):
    q = math.log2(abs((operation(a, b, n * 2) - operation(a, b, n)))) - math.log2(abs(operation(a, b, n * 4) - operation(a, b, n * 2)))
    return (operation(a, b, n * 2) * 2**q - operation(a, b, n)) / (2**q -1)
    
for i in range(len(n)):
    print(richordson(0, 3, int(n[i]), f_pramougolnik), end=' pramougolnik\n')
    print(richordson(0, 3, int(n[i]), f_centr_pramougolnik), end=' centr_pram\n')
    print(richordson(0, 3, int(n[i]), f_trapeci), end=' trapeci\n')
    print(richordson(0, 3, int(n[i]), f_simpson), end=' simpson\n')
    