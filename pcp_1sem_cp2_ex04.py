"""04. (2,5 pontos)
Você foi contratado para criar um sistema de RH que calcula o salário final de um
funcionário com base em diversos fatores: cargo, horas extras, faltas, bônus e
descontos.
Requisitos:
1. O programa deve solicitar:
o Nome do funcionário
o Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário)
o Salário base (float)
o Total de horas extras trabalhadas
o Total de faltas no mês
o Se recebeu bônus por desempenho (s ou n)
2. Regras de cálculo:
o Valor da hora extra:
▪ 1.5% do salário base por hora extra
o Desconto por falta:
▪ 2% do salário base por falta
o Bônus (se aplicável):
▪ Gerente: R$ 1000
▪ Analista: R$ 500
▪ Assistente: R$ 300
▪ Estagiário: R$ 100
3. O sistema deve:
o Calcular e mostrar:
▪ Salário bruto
▪ Total de acréscimos (horas extras + bônus)
▪ Total de descontos (faltas)
▪ Salário final
Regras de Implementação:
• Crie funções como:
o def calcular_horas_extras(salario_base, horas):
o def calcular_descontos_faltas(salario_base, faltas):
o def calcular_bonus(cargo, recebeu_bonus)"""

def calc_horas_extras(salario_base, total_horas):
    return salario_base * (0.015 * total_horas)

def calc_desconto_falta(salario_base, num_faltas):
    return salario_base * (0.02 * num_faltas)

def calc_bonus(cargo):
    match cargo:
        case 1:
            return 1000
        case 2:
            return 500
        case 3:
            return 300
        case 4:
            return 100

    return  0

def calc_salario(salario_base, acre, desc):
    return salario_base + acre - desc

nome = input("Digite o nome do funcionário: ")
cargo = int(input("Insira o cargo do funcionário: \n\n1-Gerente\n2-Analista\n3-Assistente\n4-Estagiário\n\n"))
salarioBase = float(input("Digite o salário base do funconário: "))
totalHrsExtras = int(input("Total de horas extras: "))
faltas = int(input("Total de faltas no mês: "))
bonus = input("Bônus por desempenho? (s ou n): ")

if bonus == "s":
    acrescimos = calc_horas_extras(salarioBase, totalHrsExtras) + calc_bonus(cargo)
else:
    acrescimos = calc_horas_extras(salarioBase, totalHrsExtras)

descontos = calc_desconto_falta(salarioBase, faltas)

salarioLiquido = calc_salario(salarioBase, acrescimos, descontos)

print("Funcionário:         ", nome)
print(f"Salário bruto:      R$ {salarioBase:.2f}")
print(f"Total acrescimos:   R$ {acrescimos:.2f}")
print(f"Total descontos:    R$ {descontos:.2f}")
print(f"Salário liquído:    R$ {salarioLiquido:.2f}")