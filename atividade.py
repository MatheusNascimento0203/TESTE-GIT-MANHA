#Teste esse programa, é para saber se é par ou ímpar

numero = int(input('Digite um número inteiro: '))
numero1 = numero % 2
if numero1 == 0:
  print(f'{numero} é um número par.')
else:
  print(f'{numero} é um número ímpar.')