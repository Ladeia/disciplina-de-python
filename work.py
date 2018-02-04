#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os

arquivo = open('file.db', 'wb')
for i in range(10):
	pickle.dump(i, arquivo)
arquivo.close( )
print 'Arquivo criado com sucesso'
#raw_input('Arquivo binario criado com sucesso‘)

#n=pickle.load(arquivo)

db = {}

def show_menu():

	os.system('clear') 
	print('Existe '+ str(len(db)) + ' peças cadastradas\n\n')
	print('Escolha a opção')
	print('1 - Incluir peça')
	print('2 - Consultar peça')
	print('3 - Modificar peça')
	print('4 - Excluir peça')
	print('5 - Listar peças')
	print('6 - Sair')
	return int(raw_input(''))


def existe_registro(codigo):
	duplicated = False
	if codigo in db.keys():
		duplicated = True
	
	return duplicated	


def include():
	peca = {}

	codigo = raw_input('Digite o código da peça\n')

	if existe_registro(codigo):
		print('Já existe um item cadastrado com este código, digite outro')
		include()
	else:
		peca['codigo'] = codigo
		peca['peca'] = raw_input('Digite o nome da peça\n')
		peca['description'] = raw_input('Digite a descrição da peça\n')
		peca['quantity'] = int(raw_input('Digite a quantidade da peça\n'))
		peca['price'] = float(raw_input('Digite o preço da peça\n'))

		db[codigo] = peca

		__main__()


def show_formatted_peca(codigo):
	print('Código: ' + db[codigo]['codigo'])
	print('Nome: ' + db[codigo]['peca'])
	print('Descrição: ' + db[codigo]['description'])
	print('Quantidade: ' + str(db[codigo]['quantity']))
	print('Preço: ' + str(db[codigo]['price']))

def show():
	codigo = raw_input('Digite o codigo da peça\n')
	if existe_registro(codigo):
		show_formatted_peca(codigo)
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()
	else:
		print('Registro não encontrado')
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()


def modify():
	peca = {}

	codigo = raw_input('Digite o código da peça\n')

	if existe_registro(codigo):
		peca['codigo'] = codigo
		peca['peca'] = raw_input('Digite o nome da peça\n')
		peca['description'] = raw_input('Digite a descrição da peça\n')
		peca['quantity'] = int(raw_input('Digite a quantidade da peça\n'))
		peca['price'] = float(raw_input('Digite o preço da peça\n'))

		db[codigo] = peca

		__main__()
	else:
		print('Registro não encontrado')
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()


def delete():
	codigo = raw_input('Digite o código da peça\n')

	if existe_registro(codigo):
		del(db[codigo])
		print('Registro apagado com sucesso')
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()
	else:
		print('Registro não encontrado')
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()


def list():
	if len(db) > 0:
		for codigo in db.keys():
			show_formatted_peca(codigo)
			print('-'*10)
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()
	else:
		print('Não há registros para serem exibidos')
		trash = raw_input('pressione para voltar ao menu\n')
		__main__()


def __main__():
	option = show_menu()
	if(option == 1):
		include()
	elif(option == 2):
		show()
	elif(option == 3):
		modify()
	elif(option == 4):
		delete()
	elif(option == 5):
		list()
	elif(option == 6):
		print('Saindo do programa')
		exit()
	else:
		print('Instrução não reconhecida, tente outra opção')
		__main__()






__main__()
