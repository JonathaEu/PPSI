#Vendas  
#relVendas = (listaMoto[1], listaCliente[1])
#vendas.append(relVendas)
from pathlib import Path
import os
while True:
    if not os.path.exists('vendas'):
        os.mkdir('vendas')

    nomeVenda = input("Insira o nome do modelo vendido: \n")
    Path('vendas/{}.txt'.format(nomeVenda)).touch()
    nomeCliente = input("Insira o nome do cliente que efetuou a compra :\n")
    
    listaVenda = [nomeCliente,nomeVenda]

    res = input("Deseja continuar cadastrando mais vendas ou deseja sair? 1 para continuar, 2 para sair\n")
    if res == '2':
        break
    
    with open('vendas/{}.txt'.format(nomeVenda),'a') as f:
        f.write(str(listaVenda))





        