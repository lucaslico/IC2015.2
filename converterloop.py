import subprocess
import os
import shlex
import glob
def conversor_txt():
    onlydir = [f for f in os.listdir(os.path.join(os.getcwd())) if os.path.isdir(os.path.join(os.path.join(os.getcwd()), f))]
    list.sort(onlydir)
    onlydir = onlydir[1:len(onlydir)]
    cont = 0
    for i in range(0,len(onlydir)):
        cont += 1
        onlyfiles = [f for f in os.listdir(os.path.join(os.getcwd(),onlydir[i])) if os.path.isfile(os.path.join(os.path.join(os.getcwd(),onlydir[i]), f))]
        b = os.path.join(os.getcwd(),onlydir[i]) + '/'
        for i in range(0,len(onlyfiles)):
            onlyfiles[i] = b + onlyfiles[i]
        list.sort(onlyfiles)
        contador = len(onlyfiles)
        n = contador
        while contador > 0:
            jpg = onlyfiles[n-contador]
            txt2 = jpg.replace('.JPG','')
            txt2 = txt2.replace('.TIFF','')
            contador -= 1
            command_line = "tesseract {} {} -l por".format(jpg,txt2)
            args = shlex.split(command_line)
            subprocess.Popen(args)
        onlyfiles2 = glob.glob('*.txt')
        while len(onlyfiles2) != len(onlyfiles):
            onlyfiles2 = glob.glob('*.txt')
        contador2 = len(onlyfiles2)
        b = os.path.join(os.getcwd()) + '/'
        for i2 in range(0,len(onlyfiles2)):
            onlyfiles2[i2] = b + onlyfiles2[i2]
        list.sort(onlyfiles2)
        n2 = contador2
        while contador2 > 0:
            txt = onlyfiles2[n2-contador2]
            contador2 -= 1
            arquivo = open(txt,'r',5)
            string = "".join(str(arquivo.read()))
            string = string.replace('-\n','')
            arquivo2 = open(txt,'w',5)
            arquivo2.write(string)
            arquivo2.close()
        onlyfiles3 = glob.glob('*.txt')
        list.sort(onlyfiles3)
        for i3 in range(0,len(onlyfiles3)):
            a = onlyfiles3[i3]
            command_line2 = "mv {} {}".format(a,onlydir[i])
            args2 = shlex.split(command_line2)
            subprocess.Popen(args2)
conversor_txt()
