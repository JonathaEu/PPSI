#cadastroMotocicleta
#import pickle
contador = -1
import os
from pathlib import Path
while True:
    if not os.path.exists('CrudMotocicleta'):
        os.mkdir('CrudMotocicleta')
    nomeMoto = input("Insira o modelo da moto:  ")
    Path('CrudMotocicleta/{}.txt'.format(nomeMoto)).touch()
    anoF = input("Insira o ano de fabricação: ")
    concess = input("Insira a concessionária: ")
    
    listaMoto = [nomeMoto,anoF,concess]

    res = int(input("Deseja iniciar um novo cadastro ou sair? Digite 1 e pressione ENTER para continuar, digite 2 e pressione ENTER para sair\n"))
    if res == '2':
        break 
    with open('CrudMotocicleta/{}.txt'.format(nomeMoto),'a') as f:
        f.write(str(listaMoto))









"""
while True:
    
    arquivo = open('c:/users/Jonatha/desktop/cadastro_moto.txt','a',-1,'utf-8')
    contador = contador + 1
    moto = {}
    listaMoto = []
    moto['Indice'] = contador
    moto['Nome do Modelo'] = input("Nome do Modelo: ")
    moto["Ano de fabricacao"] = input("Ano de fabricação: ")
    moto["Concessionaria"] = input("Concessionária: ")
    resM = input("Deseja iniciar um novo cadastro ou sair? Digite C e pressione ENTER para continuar, digite S e pressione ENTER para sair\n").upper()[0]
    if resM == "S":
        break
    listaMoto.append(moto.copy())
    #'\n'.join(map(str,listaMoto))
    arquivo.write(str(listaMoto))
    arquivo.write('\n')
    #arquivo.write('\n')
    #print(arquivo)
    arquivo.close()

#try:
#linha_especifica = 0

#arquivo.write(str(listaMoto1))
#arquivo.close() 

#texto = arquivo

arquivo1 = open('c:/users/Jonatha/desktop/CRUD_moto.txt', 'r')
lines = arquivo1.readline()
line1 = arquivo1.readline()
line2 = arquivo1.readline()
line3 = arquivo1.readline()
line4 = arquivo1.readline()
arquivo1.close()
print(line1,line2,line3,line4)
#lines.insert(arquivo + "\n")

#arquivo = open('c:/users/Jonatha/desktop/CRUD_moto.txt', 'w')
#arquivo.writelines(lines)
#arquivo.close()


#print(listaMoto)
#except: 
   # print("Incapaz de adicionar ao arquivo.")




arquivo = open('c:/users/Jonatha/desktop/CRUD_moto.txt','r',-1,encoding='utf-8')
arquivo = arquivo.readline()
print(arquivo)

#ALTERAçAO#

#arquivoF = json.dumps(listaMoto, indent = 1)
#arquivo.write(arquivoF)
#arquivo.close()   
"""