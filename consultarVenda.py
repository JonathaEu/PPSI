import os
from pathlib import Path

while True:
    nomeConsulta = input("Insira o nome do modelo: ")
    #Path = ('vendas/{}'.format(nomeConsulta))
    if os.path.exists('vendas/{}'.format(nomeConsulta)):
        with open('vendas/{}'.format(nomeConsulta),'r') as f:
            consulta = f.readlines()
            print(consulta)
    else:
        print("Essa venda não existe no registro")

    res = input("Deseja continuar consultando mais vendas ou deseja sair? 1 para continuar, 2 para sair\n")
    if res == '2':
        break