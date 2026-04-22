"""Exercício 2:
Faça um programa que leia 3 valores que representam os lados de um triângulo A, Be C.
ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos:
Se A≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
Se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO;
Se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO;
Se A2 <B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO;
Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;
"""

def triangulo(lado_A, lado_B, lado_C):

    if lado_A < lado_B:
        temp = lado_A
        lado_A = lado_B
        lado_B = temp

    if lado_B < lado_C:
        temp = lado_B
        lado_B = lado_C
        lado_C = temp

    if lado_A < lado_B:
        temp = lado_A
        lado_A = lado_B
        lado_B = temp

    print(f"lado A: {lado_A}, lado B: {lado_B}, lado C: {lado_C}.")

    if lado_A >= lado_B + lado_C:
        print(f"{lado_A} >= {lado_B + lado_C}")
        print("Não forma triângulo")

        return
    
    if lado_A**2 == lado_B**2 + lado_C**2:
        print("Triângulo Retângulo")
    elif lado_A**2 > lado_B**2 + lado_C**2:
        print("Triângulo Obtusângulo")
    elif lado_A**2 < lado_B**2 + lado_C**2:
        print("Triângulo Acutângulo")

    if lado_A == lado_B and lado_C == lado_B:
        print("Triângulo Equilátero")
    elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
        print("Triângulo Isóceles")

A = float(input("Digite o primeiro Lado: "))
B = float(input("Digite o segundo Lado: "))
C = float(input("Digite o terceiro Lado: "))

triangulo(A, B, C)