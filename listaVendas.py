import os
from pathlib import Path

if os.path.exists('vendas'):
    listaVenda = os.listdir('vendas')
    print(listaVenda)