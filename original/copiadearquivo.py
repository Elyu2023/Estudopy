#listar arquivos 
import os 
arquivos = os.listdir()
print(arquivos)

#copiar 
import shutil
#shutil.copy2('entrada.txt' , 'testedecopiapy/entrada.txt')

#lista de arquivos 
lista_arquivos = os.listdir()

for arquivo in lista_arquivos:
  if 'py' in arquivo:
    # if '123' in arquivo:
    #jogar para pasta testedecopia
    shutil.copy2( arquivo,'pastanova')
  





