import os
import enchant

pt = enchant.Dict('pt_BR')
en = enchant.Dict('en_US')

def taxa(): #programa que devolve a taxa de erro
    erro = []
    total = []
    onlyfiles = [f for f in os.listdir('/home/lucas/FGV/IC/txt py/') if os.path.isfile(os.path.join('/home/lucas/FGV/IC/txt py/', f))] #varia de acordo com a pasta
    contador = len(onlyfiles)
    n = contador
    while contador > 0:
        a = []
        txt = onlyfiles[n-contador]
        contador -= 1
        arquivo = open(txt, 'r',5)
        leitura = arquivo.read()
        subtotal = leitura.split()
        total.append(len(subtotal))
        for i in range(0,len(subtotal)):
            if pt.check(subtotal[i]) == False:
                if en.check(subtotal[i]) == False:
                    a.append(pt.check(subtotal[i]))
        erro.append(len(a))
    e = sum(erro)
    t = sum(total)
    print float(e)/float(t)
