"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
"""

car_away =int(input('Введите сколько километров машина проехжает за день: '))
away = int(input('Введите сколько километров составляет весь маршрут: '))
day = (away + car_away - 1) // car_away

# print(f'Количество дней за скока машина проедет весь путь: {day}')
print ((away // car_away) + int((away % car_away) != 0))
