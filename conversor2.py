'''Este conversor carrega direto de jpg para txt, sem passar por tiff'''
import os
import subprocess
import shlex

def conversor_txt(): #programa que converte arquivos de imagem para TXT
    onlyfiles = [f for f in os.listdir('/home/lucas/FGV/IC/image/') if os.path.isfile(os.path.join('/home/lucas/FGV/IC/image/', f))] #lista dos arquivos da pasta\n",
    contador = len(onlyfiles)
    n = contador
    while contador > 0:
        jpg = onlyfiles[n-contador]
        contador -= 1
        command_line = "tesseract {} texto{} -l por".format(jpg,n-contador)
        args = shlex.split(command_line)
        subprocess.Popen(args)
        
