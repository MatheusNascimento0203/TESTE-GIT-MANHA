#Um teste para saber se a letra é vogal ou consoante

letra = str(input('Digite uma letra: '))
vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', "I", 'O', 'U']
if letra in vogal:
  print('A letra digitada é uma vogal.')
else:
  print('A letra digitada é uma consoante.')