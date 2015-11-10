#codigo que corrige os erros por um app

def teste (x):
    v = SpellChecker("pt_BR",x)
    c = CmdLineChecker()
    c.set_checker(v)
    c.run()
    return v.get_text()
