def mv(): #move os arquivos para a pasta
    onlyfiles2 = glob.glob('*.txt')
    for i in range(0,len(onlyfiles2)):
        a = onlyfiles2[i]
        command_line = "mv {} txt_py".format(a)
        args = shlex.split(command_line)
        subprocess.Popen(args)
mv()
def dim_erros(): #diminui erros 
    onlyfiles = [f for f in os.listdir(os.path.join(os.getcwd(),'txt_py')) if os.path.isfile(os.path.join(os.path.join(os.getcwd(),'txt_py'), f))]
    contador = len(onlyfiles)
    b = os.path.join(os.getcwd(),'txt_py') + '/'
    for i in range(0,len(onlyfiles)):
        onlyfiles[i] = b + onlyfiles[i]
    list.sort(onlyfiles)
    n = contador
    while contador > 0:
        txt = onlyfiles[n-contador]
        contador -= 1
        arquivo = open(txt, 'r',5)
        string = "".join(str(arquivo.read()))
        string = string.replace('-\n','')
        arquivo2 = open(txt,'w',5)
        arquivo2.write(string)
        arquivo2.close()
dim_erros()
def taxa(): #programa que devolve a taxa de erro
    erro = []
    total = []
    b = os.path.join(os.getcwd(),'txt_py') + '/'
    onlyfiles = [f for f in os.listdir(os.path.join(os.getcwd(),'txt_py')) if os.path.isfile(os.path.join(os.path.join(os.getcwd(),'txt_py'), f))]
    for i in range(0,len(onlyfiles)):
        onlyfiles[i] = b + onlyfiles[i]
    list.sort(onlyfiles)
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
taxa()
