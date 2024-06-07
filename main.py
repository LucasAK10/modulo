# faz as importações
import os
from modulo import *

# programa principal
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('opção desejada: ')

        match opcao:
            case '1':
                b = int(input('Base do Quadrilátero: '))
                h = int(input('Altura do quadrilátero: '))
                print (f'Área: {calcular_quadrilatero(b,h)}')
                continue
            case '2':
                r = int(input('Raio do Círculo: '))
                print(f'Área: {calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Área: {calcular_circulo(b,h)}')
                continue
            case '4':
                b_menor = int(input('Base menor do trapézio: '))
                b_maior = int(input('Base maior do trapézio: '))
                h = int(input('Altura do trapézio: '))
                print (f'Área = {calcular_trapezio(b_menor,b_maior,h)}')
                continue 
            case '5':
                print(f'Programa Encerrado!')
                break
               













