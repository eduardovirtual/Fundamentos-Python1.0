#Desafio05
#Faça um programa que leia um número inteiro e mostre na tela o seu
#sucessor e antecessor

num = int(input('Digite um número: '))
suc = num + 1
ant = num - 1
print('O sucessor de {} é {}, e o antecessor de {} seria {}'.format(num, suc, num, ant))