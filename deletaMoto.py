import os
from pathlib import Path
while True:
    nomeMoto = input('Insira o nome do Moto a ser deletado: ')
    fP = Path('CrudMotocicleta/{}.txt'.format(nomeMoto))
    fP.unlink()
    res = input("Deseja continuar deletando mais Motos ou deseja sair? 1 para continuar, 2 para sair")
    if res == '2':
        break
    print("Motocicleta removida com sucesso")