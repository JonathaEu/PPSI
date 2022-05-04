#CrudClient
#contador = -1

import os
from pathlib import Path
while True:
    if not os.path.exists('CrudCliente'):
        os.mkdir('CrudCliente')
    nomeCliente = input("Insira nome do cliente: ")
    Path('CrudCliente/{}.txt'.format(nomeCliente)).touch()
    cpf = input("Insira o CPF do cliente: ")
    contato = input("Insira o contato: ")
    
    listaCliente = [nomeCliente,cpf,contato ]

    res = (input("Deseja iniciar um novo cadastro ou sair? Digite 1 e pressione ENTER para continuar, digite 2 e pressione ENTER para sair\n"))    
    if res == "2":
        break 
    with open('CrudCliente/{}.txt'.format(nomeCliente),'a') as f:
        f.write(str(listaCliente))