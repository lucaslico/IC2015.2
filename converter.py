'''Este conversor carrega direto de jpg para txt, sem passar por tiff
Temos primeiro de usar o programa conversor, pois ele continua fazendo os arquivos depois de rodar o programa'''
import subprocess
import os
import shlex
mk = shlex.split('mkdir txt_py')
subprocess.Popen(mk)
def conversor_txt(): #programa que converte arquivos de imagem para TXT
    onlyfiles = [f for f in os.listdir(os.path.join(os.getcwd(),'img_py/')) if os.path.isfile(os.path.join(os.path.join(os.getcwd(),'img_py/'), f))]
    b = os.path.join(os.getcwd(),'img_py') + '/'
    for i in range(0,len(onlyfiles)):
        onlyfiles[i] = b + onlyfiles[i]
    list.sort(onlyfiles)
    contador = len(onlyfiles)
    n = contador
    while contador > 0:
        jpg = onlyfiles[n-contador]
        contador -= 1
        command_line = "tesseract {} texto{} -l por".format(jpg,n-contador)
        args = shlex.split(command_line)
        subprocess.Popen(args)
conversor_txt()
