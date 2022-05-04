import os
from pathlib import Path
while True:
    nomeCliente = input('Insira o nome do cliente a ser deletado: ')
    fP = Path('CrudCliente/{}.txt'.format(nomeCliente))
    fP.unlink()
    res = input("Deseja continuar deletando mais clientes ou deseja sair? 1 para continuar, 2 para sair")
    if res == '2':
        break
    print("Cliente removido com sucesso")