"""Faça um programa que recebe:
- o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
- o peso da carga do caminhão em toneladas
- o código da carga, supondo que é um número inteiro de 10 e 40
Seu programa deve calcular:
- o peso da carga do caminhão convertido em quilos
- o preço da carga do caminhão
- valor do imposto que é cobrado com base no preço da carga e do estado de origem
- o valor total transportado pelo caminhão (carga + impostos)
Utilize as tabelas abaixo:
estado - imposto
1      -   35%
2      -   25%
3      -   15%
4      -   5%
5      -   Isento
código da carga - preço por kg
10 a 20         -   100,00
21 a 30         -   250,00
31 a 40         -   340,00

Obs.: considere que o usuário irá digitar tudo corretamente."""

def calculo_imposto(codigo_estado):
    if codigo_estado == 1:
        return  35
    elif codigo_estado == 2:
        return  25
    elif codigo_estado == 3:
        return  15
    elif codigo_estado == 4:
        return  5
    else:
        return  0

def calculo_preco_kg(codigo_carga):
    if codigo_carga < 21:
         return 100
    elif codigo_carga < 31:
         return 250
    else:
         return 340

def caminhao(preco_kg, peso_carga_toneladas, imposto):
    peso_kg = peso_carga_toneladas * 1000
    preco_total = peso_kg * preco_kg
    valor_imposto = preco_total * (imposto / 100)
    valor_final = preco_total - valor_imposto

    print(f"\nO peso total do caminhão em quilogramas é: {peso_kg:.2f} Kg")
    print(f"O preço da carga sem imposto é: R$ {preco_total:,.2f}")
    print(f"O percentual de imposto é: {imposto:}%")
    print(f"O valor final que será recebido é: R$ {valor_final:,.2f}")

cod_estado = int(input("Digite o código do estado (entre 1 à 5): "))
cod_carga = int(input("Digite o código de carga (entre 10 à 40): "))
peso_ton = float(input("Digite o peso em tonelada: "))

taxa_imposto = calculo_imposto(cod_estado)
preco_carga = calculo_preco_kg(cod_carga)

caminhao(preco_carga, peso_ton, taxa_imposto)