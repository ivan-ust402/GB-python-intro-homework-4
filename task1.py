"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

def get_salary(output, wage_rate, bonus):
    """
    Функция расчета заработной платы сотрудника
    :param output: выработка в часах
    :param wage_rate: ставка в час
    :param bonus: премия
    :return: зарплата
    """
    try:
        salary = int(output) * int(wage_rate) + int(bonus)
    except ValueError:
        return 'Введены неверные значения'
    return salary


name, production, rate, premium = argv
print(f'Заработная плата сотрудника: {get_salary(production, rate, premium)}')
