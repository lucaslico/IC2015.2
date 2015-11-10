#Função para converter imagens para tiff pelo pacote PIL do python. Muito 
#limitada ainda pois só converte imagem por imagem. E o nome final também teria 
#de ser convertido um por um.
import Image

def conversor_tif (filename):
    image = Image.open(filename)
    image.save('foto.tiff')
conversor_tif('foto.jpg')

#Second Try = getting there

#função para converter imagens para tiff pelo terminal
#Está mais avançado, pois já converte todos os arquivos na terminação .jpeg, 
#.png, .jpg, .pdf e .gif para .tiff. Mas o nome final pode ser melhorado.
#Também depende do executável estar na mesma pasta que as imagens a serem 
#convertidas. Além disso, gostaria que os novos arquivos fossem salvos noutra
#pasta
import os

def conversor_tif2 ():
    os.system("for file in *.JPG; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.pdf; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.gif; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.png; do convert $file -resize 2000 new-$file.tiff; done")    
    os.system("for file in *.jpeg; do convert $file -resize 2000 new-$file.tiff; done")    

conversor_tif2()

#função para chamar o Tesseract-ocr do Linux e aplicar nos arquivos .tiff
'''
Continua tendo a condição do executável estar na mesma pasta que os arquivos
.tiff e continua tendo o problema de criar arquivos .JPG.tiff.txt no final
'''
def tess ():
    os.system("for file in *.tiff; do tesseract $file ocr-$file;done")

tess()

import Image 
import os

def conversor_tif (filename):#esta sobrepondo
    image = Image.open(filename)
    image.save(filename + '.tiff')
def conversor_tif2 ():
    os.system("for file in *.JPG; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.pdf; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.gif; do convert $file -resize 2000 new-$file.tiff; done")
    os.system("for file in *.png; do convert $file -resize 2000 new-$file.tiff; done")    
    os.system("for file in *.jpeg; do convert $file -resize 2000 new-$file.tiff; done")
def tess ():
    os.system("for file in *.tiff; do tesseract $file ocr-$file;done")
