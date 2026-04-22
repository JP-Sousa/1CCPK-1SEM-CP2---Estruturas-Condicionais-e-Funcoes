"""Exercício 5

Você foi contratado para desenvolver um sistema simples de um banco que analisa e calcula um financiamento com parcelas fixas.
Requisitos:

1. O programa deve solicitar:
o Nome do cliente
o Idade
o Renda mensal
o Valor desejado do empréstimo
o Número de parcelas (3 até 24)

2. Regras para aprovação:
o O cliente só será aprovado se:
▪ Ter mais de 18 anos
▪ O valor do financiamento for de no máximo 20 vezes a renda
mensal

3. Taxa de juros:
o até 6 parcelas → 5% ao mês
o de 7 até 12 parcelas → 8% ao mês
o de 13 até 24 parcelas → 10% ao mês

4. Cálculo do financiamento (parcelas fixas):
o Para calcular o valor da parcela, utilize a fórmula:
▪ 𝑃𝑀𝑇 = 𝑃𝑉 ⋅    𝑖(1+𝑖)𝑛
                (1+𝑖)𝑛−1
▪ PMT → valor da parcela (PMT significa Payment/Pagamento)
▪ PV → valor financiado (PV significa Present Value, valor inicial
da dívida)
▪ i → taxa de juros (em decimal de 0 até 1)
▪ n → número de parcelas

5. O sistema deve:
Informar se o empréstimo foi aprovado ou negado
Se aprovado:
▪ Nome do cliente
▪ Valor financiado
▪ Taxa de juros aplicada
▪ Valor da parcela
▪ Valor total pago
▪ Total de juros pagos

6. Cálculos adicionais:
o Total pago:
▪ 𝑡𝑜𝑡𝑎𝑙 = 𝑃𝑀𝑇 ⋅ 𝑛
o Juros pagos:
▪ 𝑗𝑢𝑟𝑜𝑠 = 𝑡𝑜𝑡𝑎𝑙 − 𝑃𝑉

Regras de Implementação:
• Crie funções como:
def pode_aprovar(idade, renda, valor):
def definir_taxa(parcelas):
def calcular_parcela(valor, taxa, parcelas):
def calcular_total(parcela, parcelas):
def calcular_juros(total, valor):

A fórmula usada no financiamento (Tabela Price) existe para resolver um problema
prático dos bancos: transformar uma dívida com juros compostos em parcelas
iguais ao longo do tempo.
Quando uma pessoa pega um valor emprestado, os juros são aplicados mês a
mês sobre o saldo devedor. Ou seja, a dívida cresce com o tempo. Ao mesmo
tempo, o cliente precisa pagar essa dívida em parcelas fixas, que caibam no
orçamento.
A fórmula equilibra essas duas coisas: ela considera o valor inicial, a taxa de juros
e o número de parcelas, e calcula uma prestação que permanece constante.
Mesmo sendo fixa, cada parcela é composta por duas partes: uma de juros e outra
de amortização (pagamento da dívida). No início, paga-se mais juros; no final,
paga-se mais da dívida.
Por isso, essa fórmula é amplamente usada em financiamentos de carros, imóveis
e empréstimos em geral: ela permite organizar uma dívida com juros compostos
em pagamentos previsíveis e iguais."""



def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= 20 * renda:
        print("Financiamento Aprovado")

        return True
    else:
        print("Financiamento Negado")

        return  False

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas > 12:
        return 0.1
    else:
        return 0.08

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * ((1 + taxa)**parcelas)) / (((1 + taxa)**parcelas) - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

def exibir_final(nome_cliente,valor,taxa,val_parcela,total,juros):
    print(f"\nNome do cliente: {nome_cliente}")
    print(f"Valor financiado: R$ {valor:,.2f}")
    print(f"Taxa de Juros Aplicada: {taxa * 100:.0f}%")
    print(f"Valor da parcela: R$ {val_parcela:,.2f}")
    print(f"Total a ser pago: R$ {total:,.2f}")
    print(f"Total de Juros: R$ {juros:,.2f}")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do empréstimo desejado: "))
qntd_parcelas = int(input("Digite a quantidade de parcelas (entre 3 à 24): "))

aprovado = pode_aprovar(idade, renda, emprestimo)

if aprovado:
    taxa = definir_taxa(qntd_parcelas)
    parcela = calcular_parcela(emprestimo, taxa, qntd_parcelas)
    total = calcular_total(parcela, qntd_parcelas)
    juros = calcular_juros(total, emprestimo)

    exibir_final(nome, emprestimo, taxa, parcela, total, juros)