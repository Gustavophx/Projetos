import random
import os

dado = ''
lista_opcao = ['']


class Listas:
    nomes = ['Ana', 'Bia', 'Clara', 'Diana', 'Erica']
    emails = ['Ana@gmail.com', 'Bia@gmail.com',
              'Clara@gmail.com', 'Diana@gmail.com', 'Erica@gmail.com']
    telefones = ['(11)123456789', '(22)123456789',
                 '(33)123456789', '(44)123456789', '(55)123456789']
    cidades = ['São Paulo', 'Rio de Janeiro',
               'Salvador', 'Goiania', 'Curitiba']
    estados = ['Goias', 'Bahia', 'Mato Grosso', 'Amazonas', 'Sergipe']


def opcoes():
    print('Escolha uma ou mais opções abaixo a serem geradas aleatótiamente: ')
    print('[1] - Nome \n[2] - Email \n[3] - Telefone \n[4] - Cidade \n[5] - Estado')
    opcao = input('Digite uma(as) opções: ').replace(',', "")

    return opcao


print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar" ')
print('-'*83)

while True:
    opcao = opcoes()
    if opcao != 'parar':
        for item in opcao:
            if item == '1':
                dado = random.choice(Listas.nomes)
                print(dado)
            elif item == '2':
                dado = random.choice(Listas.emails)
                print(dado)
            elif item == '3':
                dado = random.choice(Listas.telefones)
                print(dado)
            elif item == '4':
                dado = random.choice(Listas.cidades)
                print(dado)
            elif item == '5':
                dado = random.choice(Listas.estados)
                print(dado)
            lista_opcao.append(dado)
        salva_dados = input(
            'Deseja salvar os adados em um arquivo? Digite s/n: ')
        if salva_dados == 's':
            with open('dados.txt', 'a') as arquivo:
                for opcao in lista_opcao:
                    arquivo.write(f'{opcao}\n')

    else:
        print('Saindo do programa...')
        break
