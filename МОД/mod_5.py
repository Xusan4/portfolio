import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Метод Рунге-Кутты 2-го порядка
def func(t, y, z):
    return z, (-t**2 * y**3 - 2*t*z)/t**2

y = 1.0   # начальное значение y
z = 0.0   # начальное значение dy/dt
t = 0.1   # начальное значение времени
h = 0.1   # шаг интегрирования
n = 100   # количество шагов
t_values = [t]
y_values = [y]
for i in range(n):
    k1 = z
    l1 = (-t**2 * y**3 - 2*t*z)/t**2
    k2 = z + h*l1
    l2 = (-t**2 * (y + 0.5*h*k1)**3 - 2*t*(z + 0.5*h*l1))/(t**2)
    
    y += h*k2
    z += h*l2
    t += h
    
    t_values.append(t)
    y_values.append(y)
    
    print(f't = {t:.4f}, y = {y:.6f}')
    
# Встроенный метод
def f(y, t):
    y1, y2 = y
    return [y2, (-t**2 * y1**3 - 2*t*y2)/t**2]
ode = odeint(f, [1, 0], t_values)
print(ode)
y1 = ode[:,0]
y2 = ode[:,1]
fig = plt.figure(facecolor='white')
plt.plot(t_values, y1, label='y(t)_vstr')


plt.plot(t_values, y_values, label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t), dy/dt(t)')
plt.title('Решение дифференциального уравнения методом Рунге-Кутты 2-го порядка')
plt.legend()
plt.grid(True)
plt.show()


