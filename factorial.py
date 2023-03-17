# -*- coding: utf-8 -*-
"""recursión: una función puede ejecutarse a si misma dentro de ella
5! = 5*4*3*2*1
4! = 4*3*2*1
5! = 5*4!
   4!=4*3!
    3!=3*2!
      2!=2*1!
         1=1*0!"""


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(input('Escribe un número: '))

    result = factorial(number)

    print(result)