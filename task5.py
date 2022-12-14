"""
5) Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая
границы). Необходимо получить результат вычисления произведения всех элементов
списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def mult_elem(el_prev, el_current):
    """
    Функция перемножения предыдущего элемента списка на текущий
    :param el_prev: предыдущее значение списка
    :param el_current: текущее значение списка
    :return: результат умножения входных параметров
    """
    return el_prev * el_current


result = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Наш список: {result}')
print(f'Результат перемножения всех элементов: {reduce(mult_elem, result)}')
