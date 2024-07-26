import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_bvp
N = 3
L = 1
T = 1
t_start = 0
t_max = 1
x_start = 0
x_end = 1
delta_x = L/N

# Т образный метод сетки
delta_t = delta_x**2/(2 * 3)
# print(delta_t)
n = int(t_max / delta_t)
# print(n)
t = np.zeros(n)
x = np.zeros(N+1)
u = np.zeros((n, N+1))
# координаты по х и начальные условия
for i in range(N+1):
    if i == 0:
        x[i] = x_start
    else:
        x[i] = x[i-1] + delta_x
    u[0][i] = 0
# координаты по t и граничные условия
for j in range(n):
    if j == 0:
        t[j] = t_start
    else:
        t[j] = t[j-1] + delta_t
    u[j][0] = math.sin(math.pi * t[j])
    u[j][-1] = 0
u_neyavniy_start = u.copy() # для решение неявным методом
# находим значения функции по итерациям времени
for j in range(1, n):
    for i in range(1, N):
        u[j][i] = 3 * delta_t * (u[j-1][i+1] - 2 * u[j-1][i] + u[j-1][i-1]) / delta_x**2 + u[j-1][i] + delta_t * t[j] * math.sin(math.pi * x[i]**2)

def solve_matric(j):
    matric = np.zeros((N, N+1))
    for i in range(N):
        for k in range(N+1):
            if i == k:
                matric[i][k] = 1 + 2 * (3 * delta_t / delta_x ** 2)
            elif i + 1 == k or i - 1 == k:
                matric[i][k] = - (3 * delta_t / delta_x ** 2)
            else:
                matric[i][k] = 0
        if i == 0:
            matric[i][-1] = u[j][i+1] + u[j][0] + delta_t * t[j] * math.sin(math.pi * x[i]**2)
        elif i == N:
            matric[i][-1] = u[j][i+1] + u[j][N] + delta_t * t[j] * math.sin(math.pi * x[i]**2)
        else:
            matric[i][-1] = u[j][i+1] + delta_t * t[j] * math.sin(math.pi * x[i]**2)
            
            
    # решение матрицы
    for i in range(N):
        # print(matric[i][i], end='^')
        if matric[i][i] != 1:
            delitel = matric[i][i]
            for j in range(N+1):
                # print(matric[i][j], end='-')
                matric[i][j] /= delitel
                # print(matric[i][j])
        for j in range(i+1, N):
            if matric[j][i] != 0:
                for k in range(N+1):
                    mnojitel = matric[j][i]
                    matric[j][k] -= matric[i][k] * mnojitel  
    # print(matric)


    new_mat = [0] * (N)
    for i in range(N):
        new_mat[i] = [0] * (N +1)
    for i in range(N):
        for j in range(N+1):
            if j < N:
                new_mat[i][j] = matric[-i-1][-j-2]
            else:
                new_mat[i][j] = matric[i][j]
    for i in range(N):
        for j in range(i+1, N):
            if new_mat[j][i] != 0:
                for k in range(N+1):
                    mnojitel = new_mat[j][i]
                    new_mat[j][k] -= new_mat[i][k] * mnojitel
    # print(new_mat)
    end_u = np.zeros(N+1)
    for i in range(1, N+1):
        end_u[i] = matric[i-1][-1]
        # print(f'X_{i+1} = {matric[i-1][-1]}')
    return end_u
new_u = []
for j in range(n):
    r = solve_matric(j)
    new_u.append(list(r))
# print(new_u)
# print(type(u))
# print(type(np.array(new_u)))
# print(u)
# print("\n\n\n")
# print(u_neyavniy_start)
# print("\n\n\n")
# print(np.array(new_u))
# print("\n\n\n")
# print(np.array(new_u) + u_neyavniy_start)
# print("\n\n\n")
# print(np.array(new_u) + u_neyavniy_start - u)


#Построение 3D-графика
x_graph, t_graph = np.meshgrid(x, t)
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(x_graph, t_graph, u, cmap='coolwarm')
ax1.set_xlabel('x')
ax1.set_ylabel('t')
ax1.set_zlabel('u')
ax1.set_title('3D Surface Plot')
ax1.set_facecolor('green')

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(x_graph, t_graph, u, cmap='coolwarm')
ax2.set_xlabel('x')
ax2.set_ylabel('t')
ax2.set_zlabel('u')
ax2.set_title('3D Surface Plot')
ax2.set_facecolor('green')
plt.show()

    