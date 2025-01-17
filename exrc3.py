N = 3.14159 # variavel do PI
raio = float(input()) # variavel do input que vai ser digitado que é float (com casas decimais)
area = N * (raio * raio) # calculo da area , porem poderia ser feita  =    area = N * (rio **2)
print(f"A={area:.4f}") # area:.4f formação para 4 area decimais



"""
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

Exemplos de Entrada	Exemplos de Saída
2.00

A=12.5664

100.64

A=31819.3103

150.00

A=70685.7750

"""