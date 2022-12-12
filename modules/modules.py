## import module example
import datetime
from datetime import timedelta
from example_module import sum, rest
from colorama import Fore, Style

# import from python.                   https://docs.python.org/3/library/
print(datetime.date.today)              # return 2022-12-16
print(timedelta(minutes=70))            # return 1:10:00

# import from own modules.                  
sum(1, 2)                               # return 3
rest(2, 1)                              # return 1

# import from pip modules.              https://pypi.org/
print(Fore.RED + "example")             # return "example" but red.