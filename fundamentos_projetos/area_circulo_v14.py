#! python
from math import pi
import sys
import errno


def help():
    print("É necessário informar o raio do círculo")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


def circulo(raio):  # É uma palavra reservada que define uma função.
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo', area)
