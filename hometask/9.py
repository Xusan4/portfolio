import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.

print('Первая задача')
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# математический метод
n = len(zp)
b1 = (n * np.sum(zp * ks) - np.sum(zp) * np.sum(ks)) / (n * np.sum(zp**2) - (np.sum(zp))**2)
b0 = np.mean(ks) - b1 * np.mean(zp)
print('y = {} + {} * x'.format(b0, b1))
print(b0 + b1 * zp)
ks_pred = b0 + b1 * zp
mse = ((ks - ks_pred)**2).sum()/n
print(mse)

# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

print('\nВторая задача')
def mse (b1, ks = ks, zp = zp, n = n):
    return np.sum((b1 * zp - ks)**2 / n)
alfa = 1e-6
b1 = 0.1
for i in range(50000):
    b1 -= alfa * (2/n) * np.sum((b1 * zp - ks) * zp)
print(b1)
print(mse(b1))

# 3. Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

print('\nТретья задача')
model = LinearRegression()

zp = zp.reshape(-1, 1)
regres = model.fit(zp, ks)

print(regres.intercept_)
print(regres.coef_)