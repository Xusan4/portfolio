import math
from sympy import  Poly, symbols, diff, sin
import numpy as np
from math import pi
import matplotlib.pyplot as plt

x = symbols('x')
n = int(input())
xi = [float(i) for i in input().split()]
cory = []
# вычисляем координаты х и у
def y(x):
    return math.sin(x*pi)
# функция синуса для графика
def func(x):
    return np.sin(x)
for i in range(len(xi)):
    print(f'y = {y(xi[i])}, x = {xi[i]}')
# функция строящая полинома лагранжа
def pol_lagranja(n):
    f = 0
    for i in range(n):
        g = 1
        for j in range(n):
            if i != j:
                g *= Poly((x - xi[j] * pi)/(xi[i] * pi - xi[j] * pi))
        f += g * y(xi[i])
    return f
polinom_lagr = pol_lagranja(n)
# находим координаты для нашего графика
for i in range(n):
    z = xi[i] * pi
    # print(z)
    elem = polinom_lagr.subs(x, z)
    cory.append(polinom_lagr.subs(x, z))
corx = np.arange(-pi, pi, 0.001)

coefficients_list_lagr = polinom_lagr.all_coeffs()
# функция лагранжа для графика
def f_lagr(x):
    lagr_func = 0
    for i in range(len(coefficients_list_lagr)):
        lagr_func += coefficients_list_lagr[i] * x ** (5 - i -1)
    return lagr_func
# функция дифференцирования синуса от х
def differencial_sin(x ,n):
    if n % 4 == 0:
        return np.sin(x)
    elif n % 4 == 1:
        return np.cos(x)
    elif n % 4 == 2:
        return -np.sin(x)
    elif n % 4 == 3:
        return -np.cos(x)
# функция для вычисления погрешности
def r_x(x_perem, xi, n):
    proizvedeniye = 1
    # функция которая использована для построения графика
    if type(x_perem) == np.ndarray:
        for i in range(n):
            proizvedeniye *= ((x_perem - xi[i]) * pi) / (i + 1)
        return abs(differencial_sin(x_perem, n) * proizvedeniye)
    # функция которая использована для построения точек в графике
    else:
        x = symbols('x')
        func_org = sin(x)
        for i in range(n):
            proizvedeniye *= ((x_perem - xi[i]) * pi) / (i + 1)
        return abs(float(func_org.diff(x, n).subs(x, x_perem)) * proizvedeniye)
# функция для вычисления погрешности лагранжа
def pogr_lagr(x):
    return abs(func(x * pi) - f_lagr(x * pi))

# вводные данные для полинома ньютона
m = int(input())
zi = [float(i) for i in input().split()]
# y = [0, 1, 3]

for i in range(len(zi)):
    print(f'y = {y(zi[i])}, x = {zi[i]}')
# функция для вычисления разделенной разности
def f_raznost(m):
    sum = 0
    for i in range(m+1):
        proizvedeniye = 1
        for j in range(m+1):
            if i != j:
                proizvedeniye *= (zi[i] - zi[j]) * pi
                # print(proizvedeniye, j, end='---\n')
        # print(proizvedeniye, i, end='---\n')
        sum += y(zi[i]) / proizvedeniye
        # print(sum, i, end='+++\n')
    return sum
for i in range(m):
    print(f_raznost(i))
# функция для вычисления полинома ньютона
def nuton_pol(m):
    x = symbols('x')
    sum = 0
    for i in range(m):
        proizvedeniye = 1
        for j in range(i):
            proizvedeniye *= Poly((x - zi[j]) * pi)
            # print(proizvedeniye, i, j, end='***\n')
        # print(proizvedeniye, i, end='+++\n')
        # print(f_raznost(i), end='raznost\n')
        sum += f_raznost(i) * proizvedeniye
        # print(sum, i, end='===\n')
    return sum
polinom_nuton = nuton_pol(m)
# print(nuton_pol(m), end='----------------------\n')
# for i in range(m):
#     print(polinom_nuton.subs(x, zi[i]))
# функция лагранжа для графика
coefficients_list_nuton = polinom_nuton.all_coeffs()
def f_nuton(x, m):
    nuton_func = 0
    for i in range(len(coefficients_list_nuton)):
        nuton_func += coefficients_list_nuton[i] * x ** (m - i -1)
    return nuton_func
# for i in range(m):
#     print(f_nuton(zi[i], m))
cory_nuton = []
for i in range(m):
    cory_nuton.append(polinom_nuton.subs(x, zi[i]))
corz = np.arange(-pi, pi, 0.001)
# функция для вычисления погрешности ньютона
def pogr_nuton(x):
    return abs(func(x * pi) - f_nuton(x, m))


# Рисуем график полинома лагранжа и самой функции
plt.figure(figsize=(16, 6))
plt.subplot(1, 3, 1)
plt.title('Графики функций')
# Ставим точки лагранжа на графике
for i in range(n):
    plt.plot(xi[i]*pi, cory[i], 'ro', markerfacecolor='w')
# рисуем график полинома лагранжа
plt.plot(corx * pi, f_lagr(corx * pi), 'r')
# Ставим точки ньютона на графике
for i in range(m):
    plt.plot(zi[i]*pi, cory_nuton[i], 'gs', markerfacecolor='w')
# рисуем график полинома ньютона
plt.plot(corz * pi, f_nuton(corz, m), 'g')
# рисуем график функции синус
plt.plot(corx * pi, func(corx * pi), 'b')
plt.xlim(-1, pi + 1)
plt.ylim(-1, pi + 1)
plt.grid()

# Рисуем оценку погрешностей для полинома Ланранжа
plt.subplot(1, 3, 2)
plt.title('Оценка погрешностей для Лагранжа')
# ставим точки в графике погрешностей для лагранжа
for i in range(n):
    plt.plot(xi[i]*pi, r_x(xi[i], xi, n), 'ro', markerfacecolor='w')
# рисуем график погрешности по формуле
plt.plot(corx * pi, r_x(corx, xi, n), 'b')
# рисуем график погрешности для лагранжа
plt.plot(corx * pi, pogr_lagr(corx), 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1, pi + 1)
plt.ylim(-0.005, 0.02)
plt.grid()


plt.subplot(1, 3, 3)
plt.title('Оценка погрешностей для Ньютона')
# ставим точки в графике погрешностей для ньютона
for i in range(m):
    plt.plot(zi[i]*pi, r_x(zi[i], zi, m), 'gs', markerfacecolor='w')
# рисуем график погрешности по формуле
plt.plot(corx * pi, r_x(corz, zi, m), 'b')
# рисуем график погрешности для ньютона
plt.plot(corz * pi, pogr_nuton(corx), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1, pi + 1)
plt.ylim(-0.005, 0.02)
plt.grid()
plt.show()
