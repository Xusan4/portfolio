from scipy.optimize import minimize
import sympy as sp
def f(x, y):
    return (x - 1)**2 + y**4/4
def df_dx(x):
    return 2 * (x0 - 1)
def df_dy(y):
    return 4 * (y**3/4)
# Ввод данных
eps = 0.001
print('Введите х: ')
x_start = float(input())
print('Введите y: ')
y_start = float(input())

# Градиентный спуск
def f_alfa(x0, y0):
    if df_dx(x0) != 0 and df_dy(y0) != 0:
        alfa_x = (x0 - 1) / df_dx(x0)
        alfa_y = y0 / df_dy(y0)
        if alfa_x < alfa_y:
            return alfa_x
        else:
            return alfa_y
    elif df_dy(y0) != 0 and df_dx(x0) == 0:
        return y0 / df_dy(y0)
    elif df_dy(y0) == 0 and df_dx(x0) != 0:
        return (x0 - 1) / df_dx(x0)
    else:
        return 1
x0 = x_start
y0 = y_start
alfa = f_alfa(x0, y0)
xi = x0 - alfa * df_dx(x0)
yi = y0 - alfa * df_dy(y0)
# print(alfa)
# print(alfa * df_dy(y0))
i = 1
while abs(yi - y0) > eps and abs(xi - x0) > eps and abs(f(xi, yi) - f(x0, y0)):
    x0 = xi
    y0 = yi
    # print(x0, y0)
    alfa = f_alfa(x0, y0)
    xi = x0 - alfa * df_dx(x0)
    yi = y0 - alfa * df_dy(y0)
    # print(xi, yi)
    i += 1
print()
print('Метод градиентного спуска: ',round(xi), round(yi))
print('Количество итераций равна = ', i)
print()

# Координатный спуск
x = sp.symbols('x')
y = sp.symbols('x')
f = (x-1)**2 + (y**4)/4
proizvodnaya_ot_x = sp.diff(f,x)
proizvodnaya_ot_y = sp.diff(f,y)
print(proizvodnaya_ot_x, proizvodnaya_ot_y)
x0 = x_start
y0 = y_start
def find_cor(num_perem, x0, y0):
    if num_perem == 1:
        return 1
    elif num_perem == 2:
        return 0
xi = find_cor(1, x0, y0)
yi = find_cor(2, x0, y0)
i = 1
while abs(yi - y0) > eps and abs(xi - x0) > eps and abs(f(xi, yi) - f(x0, y0)) > eps:
    x0 = xi
    y0 = yi
    xi = find_cor(1, x0, y0)
    yi = find_cor(2, x0, y0)
    i += 1
print('Метод покоординатного спуска: ',xi, yi)
print('Количество итераций равна = ', i)
print()
# Встроенный метод
def func(x):
    return (x[0] - 1)**2 + x[1]**4/4
initial_guess = [x_start, y_start]
result = minimize(func, initial_guess, method='Nelder-Mead')
g = result.fun
h = result.x 
print("Минимум функции:", round(g))
print("Аргументы минимума:", h)
print()




