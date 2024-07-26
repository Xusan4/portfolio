import math
import numpy as np
from scipy import stats

# 1. Когда используется критерий Стьюдента, а когда Z –критерий?

print('Критерий Стьюдента используется когда у нас не известен сигма, а Z-критерий используется когда известен сигма')

# 2. Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм. Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм. 

print('Вторая задача')
mu_zero = 17
alfa = 0.05
n = 100
mu_alter = 17.5
dispers = 4
sigma = math.sqrt(dispers)
z = (mu_alter - mu_zero) / sigma/math.sqrt(n)
print(z)
print('нулевая гепотеза истиная так как значение z меньше значения альфа')

# 3. Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г. Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190. Известно, что их веса распределены нормально. Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)

print('Третья задача')
mu_zero = 200
n = 10
z = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
alfa = 0.01
sigma = np.std(z, ddof=1)
mu_alter = np.mean(z)
t = (mu_alter - mu_zero) / (sigma / math.sqrt(n))
print(t)
print('Так как у нас модуль t меньше модуля t_alfa/2 следует что нулевоя гепотиза истина')

# 4. Есть ли статистически значимые различия в росте дочерей? Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165 Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

print('Четвертая задача')
a = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
b = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])
print(stats.ttest_ind(a, b))
print('Так как p-value значительно больше чем alfa из этого следует что нулевая гепотиза истина, и статистических различий не наблюдается')