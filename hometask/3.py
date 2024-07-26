import numpy as np
# 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
x = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
print("Первая задача:")
print(np.std(x))
print(np.var(x))
print(np.var(x, ddof=1))
print(np.mean(x))

# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

x = (5/8 * 4/7 * 5/12 * 7/11 * 6/10 * 5/9 )+ (5/8 * 3/7 * 5/12 * 4/11 * 7/10 * 6/9) + (3/8 * 2/7 * 5/12 * 4/11 * 3/10 * 7/9)
print('Вторая задача:')
print(x)

# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

p_a = 0.9 * 0.2 * 0.4 / (0.9 * 0.2 * 0.4 + 0.1 * 0.8 * 0.4 + 0.1 * 0.2 * 0.6)
p_b = 0.1 * 0.8 * 0.4 / (0.9 * 0.2 * 0.4 + 0.1 * 0.8 * 0.4 + 0.1 * 0.2 * 0.6)
p_c = 0.1 * 0.2 * 0.6 / (0.9 * 0.2 * 0.4 + 0.1 * 0.8 * 0.4 + 0.1 * 0.2 * 0.6)
print('Третья задача:')
print(p_a)
print(p_b)
print(p_c)

# 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

print('Четвертая задача:')
p_a = 1/4 * 0.8 / (1/4 * 0.8 + 1/4 * 0.7 + 2/4 * 0.9)
p_b = 1/4 * 0.7 / (1/4 * 0.8 + 1/4 * 0.7 + 2/4 * 0.9)
p_c = 2/4 * 0.9 / (1/4 * 0.8 + 1/4 * 0.7 + 2/4 * 0.9)
print(p_a)
print(p_b)
print(p_c)

# 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

print('Пятая задача:')
p_a = 0.1 * 0.2 * 0.25
p_b = (0.1 * 0.2 * 0.75) + (0.1 * 0.8 * 0.25) + (0.9 * 0.2 * 0.25)
p_extra = (0.1 * 0.8 * 0.75) + (0.9 * 0.2 * 0.75) + (0.9 * 0.8 * 0.25) # вероятность того что выйдет из строя одна деталь
p_c = p_a + p_b + p_extra
p_d = p_b + p_extra
print(p_a)
print(p_b)
print(p_c)
print(p_d)