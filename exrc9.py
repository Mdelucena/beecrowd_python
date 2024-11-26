vendedor = input()
salario_fixo = float(input())
vendas = float(input())
comissao = (15 / 100) * vendas
salario = comissao + salario_fixo

print(f"Total= R$ {salario:.2f}")