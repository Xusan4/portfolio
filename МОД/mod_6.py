import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
N = 1000
r_0 = 1
r_n = 0

#Решение системы линейных уравнений после преобразования методом конечных разностей
def solve_matric(a, b, c, d):
    n = len(b)
    c_ = np.zeros(n)
    d_ = np.zeros(n)
    x = np.zeros(n)

    c_[0] = c[0] / b[0]
    d_[0] = d[0] / b[0]

    for i in range(1, n-1):
        m = 1.0 / (b[i] - a[i-1] * c_[i-1])
        c_[i] = c[i] * m
        d_[i] = (d[i] - a[i-1] * d_[i-1]) * m

    d_[n - 1] = (d[n-1] - a[n-2] * d_[n-2]) / (b[n-1] - a[n-2] * c_[n-2])

    x[n - 1] = d_[n-1]

    for i in range(n-2, -1, -1):
        x[i] = d_[i] - c_[i] * x[i+1]

    return x

# Разностный метод
def finite_difference_method(r_0, r_n, N):
    h = 1 / N
    t = np.linspace(0, 1, N)
    A = np.zeros(N-2) # Наддиагональ
    B = np.zeros(N-2) # Главная диагональ
    C = np.zeros(N-2) # Поддиагональ
    d = np.zeros(N-2) # Вектор правой части
    
    # Заполнение векторов
    for i in range(N-2):
        A[i] =  1 / (h ** 2)
        B[i] = -2 / (h ** 2) + 1
        C[i] =  1 / (h ** 2)
        d[i] = 0

    # Применение граничных условий
    d[0] = - r_0 / (h ** 2)
    d[-1] = - r_n / (h ** 2)

    # Решение системы линейных уравнений методом прогонки
    r_interior = solve_matric(A, B, C, d)

    # Добавление граничных значений
    r = np.concatenate(([r_0], r_interior, [r_n]))

    return t, r

t, r = finite_difference_method(r_0, r_n, N)

# Решение встроенным методом
def r_prime(t, r):
    return np.vstack((r[1], -r[0]))

def boundary_conditions(r_a, r_b):
    return np.array([r_a[0] - r_0, r_b[0] - r_n])

# Начальное приближение
t_values = np.linspace(0, 1, N)
r_initial = np.zeros((2, t_values.size))
r_initial[0] = np.linspace(r_0, r_n, t_values.size)

# Решение краевой задачи методом solve_bvp
solution = solve_bvp(r_prime, boundary_conditions, t_values, r_initial)
t_plot = np.linspace(0, 1, N)
r_plot = solution.sol(t_plot)[0]
R = abs(r - r_plot)
# print(r_plot)
plt.subplot(1, 2, 1)
plt.figure(figsize=(12, 6))
plt.plot(t, r, color='r', label='сеточный метод')
plt.plot(t_plot, r_plot, color='b', label='Встроенный метод', linestyle = 'dashed')
plt.xlabel('t')
plt.ylabel('r(x)')
plt.title('Решение краевой задачи')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(t, R, color='b')
plt.grid(True)
plt.show()