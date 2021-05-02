# def estado_do_gui(qualidade):
#     print('Gui lê um comentário')
#     if qualidade == 'piada boa':
#         return 'rindo'
#     else:
#         return 'serio'
#
#
# meu_estado = estado_do_gui('piada boa')
#
# print(meu_estado)

# numeros = [1, 2, 3]
#
# futuros_devs = ['lucas', 'isabela', 'chris']
#
# print(futuros_devs[0])
# print(futuros_devs[2])
# print(futuros_devs[1])
#
# mais_devs = ['joel', 'priscila', 'rhuan']
#
# geral = futuros_devs + mais_devs
#
# print(geral)
# print(geral[-3])

# devs = ['davi', 'gabriel', 'juliana', 'ana']
#
# for dev in devs:
#     print(dev + ' manda bem no python')

frutas = ['pera', 'maca', 'laranja']

def encontra_frutas(f):
    for fruta in frutas:
        if fruta == f:
            print('Achei a fruta')
            return
        else:
            print('Ainda estou procurando')

    print('nao achei')

encontra_frutas('pera')

numeros = [1,2,3]
maisdddd