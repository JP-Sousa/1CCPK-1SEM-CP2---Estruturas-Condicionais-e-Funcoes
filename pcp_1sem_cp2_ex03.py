"""03. (2,0 pontos)
Uma instituição de ensino avalia seus alunos ao longo do semestre com base em diferentes atividades.

Requisitos:

1. O programa deve solicitar:
o Nota do Checkpoint 1 (cp1)
o Nota do Checkpoint 2 (cp2)
o Nota do Checkpoint 3 (cp3)
o Nota da Sprint 1 (sp1)
o Nota da Sprint 2 (sp2)
o Nota da Global Solution (gs)

2. O programa deve solicitar:

o Todas as notas variam de 0 a 10 e podem ser decimais
o O sistema deve identificar a menor nota entre os três checkpoints
o A menor nota deve ser desconsiderada no cálculo

3. A composição da média segue os seguintes pesos:

o 40% → média dos 2 maiores Checkpoints + 2 Sprints
o 60% → nota da Global Solution
o 40% → média do 1º semestre

4. Cálculo da média:

o A média do semestre deve ser calculada utilizando:
▪ As duas maiores notas dos checkpoints
▪ As duas notas das sprints
▪ A nota da Global Solution
o Fórmula:
o 𝑚𝑒𝑑𝑖𝑎 = (
𝑐𝑝1+𝑐𝑝2+𝑐𝑝3−𝑚𝑒𝑛𝑜𝑟+𝑠𝑝1+𝑠𝑝2
4
) ⋅ 0.4 + 𝑔𝑠 ⋅ 0.6
o Média com peso:
▪ 𝑚𝑒𝑑𝑖𝑎𝑃𝑒𝑠𝑜 = 𝑚𝑒𝑑𝑖𝑎 ⋅ 0.4"""

notacp1 = float(input("Digite a nota do Checkpoint 01 (0 a 10): "))
notacp2 = float(input("Digite a nota do Checkpoint 02 (0 a 10): "))
notacp3 = float(input("Digite a nota do Checkpoint 03 (0 a 10): "))

notasp1 = float(input("Digite a nota da Sprint 01 (0 a 10): "))
notasp2 = float(input("Digite a nota do Sprint 02 (0 a 10): "))

notags = float(input("Digite a nota do Global Solutions (0 a 10): "))

menor = notacp1

if notacp2 < menor:
    menor = notacp2
    if notacp3 < menor:
        menor = notacp3
elif notacp3 < menor:
    menor = notacp3

media_semestre = ((notacp1 + notacp2 + notacp3 - menor + notasp1 + notasp2) / 4) * 0.4 + (notags * 0.6)

media_peso = media_semestre * 0.4

print(f"Média do semestre (sem peso): {media_semestre:.2f}")
print(f"Média do semestre com peso: {media_peso:.2f}")