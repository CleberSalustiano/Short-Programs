import pickle
import os
def limpatela(): 
    if os.name == "nt":
        os.system("cls")
    else:
        os.systeam("clear") 
        
def datastrtotupla(data): #Transforma a data do imput em tupla
    if len(data) == 10:
        dia = int (data[:2])
        mes = int (data[3:5])
        ano = int (data[6:])
    elif len(data) == 8:
        dia = int (data[:2])
        mes = int (data[2:4])
        ano = int (data[4:])
    return ((dia,mes,ano))

def cadastrarmotorista(motorista): #Cadastra o motorista
    cnh = input('Digite a CNH do novo motorista: ')
    nome = input('Digite o nome: ')
    data = input('Digite a data de nascimento(dd/mm/aaaa): ')
    conf = conferir(cnh, motorista)
    if conf == True:
        data = datastrtotupla(data)
        motorista[cnh] = (nome, data)
        limpatela()
        print('CNH cadastrada com sucesso!\n')
        return True
    else:
        limpatela()
        print ('ERROR! CNH ja registrada\n')
        return False

def cadastrarveiculo(veiculos, motoristas): #Cadastra veículo
    placa = input('Digite a placa do veículo: ')
    cnh = input ('Digite a CNH: ')
    modelo = input ('Digite o modelo do carro: ')
    cor = input('Digite a cor do veículo: ')
    confplaca = conferir(placa, veiculos)
    confcnh = conferir (cnh, motoristas)
    if confplaca == True and confcnh == False:
        veiculos[placa] = (cnh, modelo, cor)
        limpatela()
        print ('Veiculo cadastrado com sucesso!\n')
        return True
    elif confplaca == False:
        limpatela()
        print('ERROR! Placa ja cadastrada.\n')
        if confcnh == True:
            print('ERROR! CNH não cadastrada\n')
        return False
    elif confcnh == True:
        limpatela()
        print('ERROR! CNH não cadastrada.\n')
        return False
    
def alterarproprietario(veiculos, motoristas): #Altera o proprietário
    placa = input('Digite a placa do veículo: ')
    cnh = input('Digite a CNH do novo proprietário: ')
    confplaca = conferir(placa, veiculos)
    confcnh = conferir(cnh, motoristas)
    if confplaca == False and confcnh == False:
        _, modelo, cor = veiculos[placa]
        veiculos[placa] = (cnh,modelo, placa)
        limpatela()
        print('Proprietário alterado com sucesso!\n')
        return True
    elif confplaca == True:
        limpatela()
        print('ERROR! Placa não cadastrada.\n')
        if confcnh == True:
            print('ERROR! CNH não cadastrada.\n') 
        return False
    elif confcnh == True:
        limpatela()
        print('ERROR! CNH não cadastrada.\n')
        return False

def cadastrarinfracao (infracoes, veiculos): #Cadastra a Infração
    data = input('Digite a data que ocorreu a infracao(dd/mm/aaaa): ')
    placa = input ('Digite a placa do veiculo envolvido: ')
    nat = int(input('''Qual a natureza da infracao?
1 - Leve
2 - Media
3 - Grave
4 - Gravissima
'''))
    data = datastrtotupla(data)
    conf = conferir (placa, veiculos)
    if conf == False:
        if nat == 1:
            nat = 'Leve'
        elif nat == 2:
            nat = 'Media'
        elif nat == 3:
            nat = 'Grave'
        elif nat == 4:
            nat = 'Gravissima'
        else:
            limpatela()
            print('ERROR! Opção de natureza inexistente.\n')
            return False
        infracoes.append((len(infracoes)+1, data, placa, nat))
        limpatela()
        print ('Infração cadastrada com sucesso\n')
        return True
    else:
        limpatela()
        print('ERROR! Placa não cadastrada\n')
        return False

def conferir (cod, dic): #Confere se existe um código em um dicionário
    if cod in dic:
        return False
    return True
    
def salvar (mot, veic, infra, nat): #Salva o arquivo bin.
    with open ('multas.bin', 'wb') as arq:
        pickle.dump(mot, arq)
        pickle.dump(veic, arq)
        pickle.dump(infra, arq)
        pickle.dump(nat, arq)

def main():
    if os.path.isfile("multas.bin"):
        with open ('multas.bin', 'rb') as arq:
            motoristas = pickle.load (arq)
            veiculos = pickle.load(arq)
            infracoes = pickle.load(arq)
            natureza = pickle.load(arq)

    menu = '''1 - Cadastrar um novo motorista
2 - Cadastrar um novo veículo
3 - Alterar proprietário de um veículo
4 - Cadastrar uma nova infração    
5 - Sair do sistema
    '''
    print(menu)
    opcao = int(input ())
    limpatela()
    cod = 0 #Recebe os return das funções contendo 0 ou 1, indicando se teve ou não alteração. Para salvar o arquivo.
    while opcao != 5:
        if opcao == 1:
            cod = cadastrarmotorista(motoristas)
        elif opcao == 2:
            cod = cadastrarveiculo(veiculos, motoristas)
        elif opcao == 3:
            cod = alterarproprietario(veiculos, motoristas) 
        elif opcao == 4:
            cod = cadastrarinfracao(infracoes, veiculos)
        else:
            limpatela()
            print('''ERROR! A opção que voce digitou não existe.
Por favor tente novamente.\n''')
        if cod == True:
            salvar (motoristas, veiculos, infracoes, natureza)
        cod = 0
        print(menu)
        opcao = int(input())
        limpatela()
main()