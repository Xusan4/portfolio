# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз
p_a = 13 / 52 * 12 / 51 * 11 / 50 * 10 / 49
p_b = 4 / 52 * 48 / 51 * 47 / 50 * 46 / 49
print(p_a, p_b)

# 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
p_two = 1 / (8 * 9 * 10)
print(p_two)

# 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?
p_three = 9 / 15 * 8 / 14 * 7 / 13
print(p_three)

# 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
p_four = 2 / 100 * 1 / 99
print(p_four)