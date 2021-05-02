
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

# def say_hello_from_kenzie():
#     print("Hello from Kenzie")
#
#
# say_hello_from_kenzie()
# say_hello_from_kenzie()
# say_hello_from_kenzie()
# say_hello_from_kenzie()
#
#
# def untar_forma():
#     forma_untada = True
#     return forma_untada
#
# def mistura_ingredientes(ovo, leite, farinha, manteiga):
#     massa = ovo + leite + farinha + manteiga
#     if untar_forma():
#         forma = massa
#     return forma
#
# def assar_bolo(forma_com_massa)
#     if temperatura_forno == 180:
#         forno = forma_com_massa
#
# ovo = 'ovo'
# leite = 'leite'
# farinha = 'farinha'
# manteiga = 'manteiga'

#mistura_ingredientes()

def multiplica(x, y):
    return x * y

resultado = multiplica(2,5)
print(resultado)

def valida_string(nome):
    if nome.islower():
        print("está capitalizado")
    else:
        print("não está tudo minusculo")

    if nome.isupper():
        print("está maiusculo")
    else:
        print('não está tudo maisculo')

    print(nome.find("avo"))
    #if nome.find('a') == -1:
        #print("a não existe na string")

    print(nome.split())
    nome_separado = nome.split()

    print(" 💛 ".join(nome_separado))

valida_string("maria foi visitar sua tia")

