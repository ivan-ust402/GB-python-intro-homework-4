"""
6) Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при
котором повторение элементов списка будет прекращено.
"""
from sys import argv
from itertools import count, cycle

# Для демонстрации ввести: python task6.py 3 5 привет 5 к
name, first_number, repeat_count, user_list_elem = argv


def iterator_count(start_number):
    """
    Итератор, генерирующий целые числа, начиная с указанного
    :param start_number: число для старта
    :return: вывод на экран целы чисел в диапазоне от входного до конечного
    (входное + 7)
    """
    finish = start_number + 7
    for el_count in count(start_number):
        if el_count > finish:
            break
        print(el_count)
    print('')


def iterator_elem(repeat_number, list_elem):
    """
    Функция повторения входной строки до указанного количества раз
    :param repeat_number: ограничение повторений
    :param list_elem: пользовательский элемент листа
    :return: вывод на экран элементов в цикле
    """
    iter_list = [list_elem]
    counter = 0
    for el_str in cycle(iter_list):
        if counter == repeat_number:
            break
        print(el_str)
        counter += 1
    print('')


def iterator_list(repeat_number, input_list):
    """
    Функция повторения каждого элемента входного листа до указанного количества
    раз
    :param repeat_number: ограничение повторений
    :param input_list: пользовательский лист
    :return: вывод на экран элементов в цикле
    """
    counter = 0
    for el_str in cycle(input_list):
        if counter == repeat_number:
            break
        print(el_str)
        counter += 1
    print('')


iterator_count(int(first_number))
iterator_elem(int(repeat_count), user_list_elem)
iterator_list(int(repeat_count), user_list_elem)
