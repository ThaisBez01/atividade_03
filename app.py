'''
Crie um programa que contole a entrada de usuários no brinquedo "Trem Fantasma" de um Parque de diversões, O programa só deve
autorizar a entrada de usuários que possuam mais de 10 anos de idade e menos de 150 kg de peso.
'''

#Nome do usuário
nome = input("Insira seu nome: ")
# Solicita a idade do usuário
idade = int(input("Insira a sua idade: "))
# Solicita o peso do usuário
peso = float(input("Insira o seu peso em kg: "))


# Verifica as condições de entrada
if idade > 10 and peso < 150:
    print("Entrada autorizada! Aproveite o Trem Fantasma!")
else:
    print("Entrada negada. Você precisa ter mais de 10 anos e pesar menos de 150 kg para entrada no brinquedo, Trem Fantasma.")