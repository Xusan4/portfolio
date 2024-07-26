import math
import numpy as np
from sympy import diff, symbols, cos, Poly
from scipy.optimize import fsolve

# Метод Ньютона
x = symbols('x')
f1 = Poly(x)
f2 = cos(x)
epsilon = 0.001
i = 0
x_i_iter = 1/2
mat_yakobi = np.array([[float(f1.diff(x).subs(x, x_i_iter)), 1.0], [float(f2.diff(x).subs(x, x_i_iter)), 1.0]])
# print(mat_yakobi, end='--\n')
inverse_yakobi = np.linalg.inv(mat_yakobi)
matrica = mat_yakobi @ inverse_yakobi
mat_func = np.array([[float(f1.subs(x, x_i_iter))], [float(f2.subs(x, x_i_iter))]])
# print(mat_func, end='+++\n')
delta_x = -inverse_yakobi @ mat_func
x_i_iter += delta_x
while abs(delta_x[0][0]) > epsilon:
    i += 1
    mat_yakobi = np.array([[float(f1.diff(x).subs(x, x_i_iter[0][0])), 1.0], [float(f2.diff(x).subs(x, x_i_iter[0][0])), 1.0]])
    # print(mat_yakobi, end='---\n')
    inverse_yakobi = np.linalg.inv(mat_yakobi)
    matrica = mat_yakobi @ inverse_yakobi
    mat_func = np.array([[float(f1.subs(x, x_i_iter[0][0]))], [float(f2.subs(x, x_i_iter[0][0]))]])
    # print(mat_func, end='+++\n')
    delta_x = -inverse_yakobi @ mat_func
    x_i_iter += delta_x
    # print(delta_x)
else:
    print(mat_func)
    print(i+1)

#метод простых итераций
x = symbols('x')
y = cos(x)
i = 0
x0 = 0.5
xi = float(y.subs(x, x0))

while abs(xi - x0) > epsilon:
    x0 = xi
    xi = float(y.subs(x, x0))
    i += 1
else:
    print(x0, xi)
    print(i)
    
    
  
# Встроенный метод
def y(w):
    func = np.zeros(2)
    func[0] = w[1] - w[0]
    func[1] = w[1] - cos(w[0])
    return func
w = [1/2, 1/2]
solution = fsolve(y, w, full_output=1)
print(solution[0])