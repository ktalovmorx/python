#-- Autor : Jose Ernesto Morales Ventura
#-- Date : 03/Jan/2020
#-- Os : Windows
#-- Python Version : 3.9

import os

class IncorrectValue(BaseException):
    def __init__(self, message):
        BaseException().__init__(message)
        self.args = (message,)

def validate(function):
    def wrapper(n):
        try:
            n = int(float(n))
            return function(n)
        except:
            raise IncorrectValue('Please, insert a correct value')
    return wrapper

@validate
def fibonacci(n):
    fib = [0]
    if n<1:n=0
    for f in range(0,n,1):
        if len(fib)==1:
            fib.append(fib[-1]+1)
        else:
            fib.append(fib[-1]+fib[-2])
    return fib, sum(fib)

while True:
    n = input('Insert an index or type EXIT to close>>>')
    if n.lower() == 'exit': break
    try:
        fb = fibonacci(n)
    except BaseException as e:
        print(e.args[0])
        continue
    print('\n',f'F({n})',f'Secuence:{fb[0]}',f'Summation:{fb[1]}', sep='\n', end='\n')
    input('\npress ENTER to continue')
    os.system('cls')

          
