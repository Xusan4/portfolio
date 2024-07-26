import numpy as np
import math
from scipy import stats

# 1. Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16. Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя M = 80, а объем выборки n = 256.

print('Первыя задача')
sigma = 16
p = 0.95
mu = 80
n = 256

t = stats.t.ppf(0.975, 255)
print(t)
z_plus = mu + t * (sigma / math.sqrt(n))
z_minus = mu - t * (sigma / math.sqrt(n))
print(z_minus, z_plus)

# 2. В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95. 

print('Вторая задача')
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
p = 0.95
sigma = np.std(a, ddof=1)
n = len(a)
t = stats.t.ppf(0.975, n-1)
mu = np.mean(a)
z_minus = mu - t * (sigma / math.sqrt(n))
z_plus = mu + t * (sigma / math.sqrt(n))
print(z_minus, z_plus)

# 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

print('Третья задача')
daughter = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mother = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
n = len(a)
p = 0.95
mu_daughter = np.mean(daughter)
mu_mother = np.mean(mother)
disp_daughter = np.var(daughter, ddof=1)
disp_mother = np.var(mother, ddof=1)
disp = (disp_daughter + disp_mother) / 2
delta = abs(mu_daughter - mu_mother)
t = stats.t.ppf(0.975, 2*(n-1))
z_minus = delta - t * math.sqrt(disp/len(daughter) + disp/len(mother))
z_plus = delta + t * math.sqrt(disp/len(daughter) + disp/len(mother))
print(z_minus, z_plus)