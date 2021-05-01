# x = 5
# y = 2
#
# print(x)
# print(y)
#
# print('hello world')
#
# z = x + y
# print(z)
#
# cor_verde = 'verde'
# cor_vermelho = 'vermelho'
#
# ola = 'youtube '
# boa_noite = 'boa noite'
# print(ola + boa_noite)
#
#
# A = False
# B = True
#
# if A:
#     print("A é maior que B")
# elif B:
#     print("B é maior que A")
# else:
#     print("B é igual a que A")

mes = input("Qual mês é o seu aniversario?")
dia = int(input("Qual o dia?"))

if mes == 'jan':
    tipo = "ground"
elif mes == 'fev':
    tipo = "fighting"

if dia == 1:
    tipo = tipo + " electric"

print(tipo)