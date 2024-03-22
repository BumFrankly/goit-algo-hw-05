import re
from typing import Callable

def generator_numbers(text:str):
    pattern = r'\b\d+(?:\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text:str, func:Callable):
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 2200.01 як основний дохід, доповнений додатковими надходженнями 527.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")