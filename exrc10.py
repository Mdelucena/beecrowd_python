# Leitura dos dados para a primeira peça
codigo1, quant_peca1, valor_peca1 = input().split()
quant_peca1 = int(quant_peca1)  # Converte a quantidade para inteiro
valor_peca1 = float(valor_peca1)  # Converte o valor para float

# Leitura dos dados para a segunda peça
codigo2, quant_peca2, valor_peca2 = input().split()
quant_peca2 = int(quant_peca2)  # Converte a quantidade para inteiro
valor_peca2 = float(valor_peca2)  # Converte o valor para float

# Cálculo do valor total
valor_pedido = (quant_peca1 * valor_peca1) + (quant_peca2 * valor_peca2)

# Exibindo o resultado com 2 casas decimais
print(f"VALOR A PAGAR: R$ {valor_pedido:.2f}")
