#listar arquivos 
import os
import shutil 
lista_arquivos = os.listdir('./original')
print(lista_arquivos)

#copiar 
import shutil
for arquivo in lista_arquivos:
    
#jogar para pasta backup
  shutil.copy2( arquivo,'./backup')
  





