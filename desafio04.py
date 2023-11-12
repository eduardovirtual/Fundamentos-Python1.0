#Desafio04
#Faça um programa que leia algo pelo teclado e mostre na tela o
#seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo desse valor é de: ', type(x))
print('É alfabético?', x.isalpha())
print('É numérico?', x.isnumeric())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('Está capitalizado?', x.istitle())
print('Só tem espaços?', x.isspace())