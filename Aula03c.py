# logica e (and)


verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print ("verifica_login")

if verifica_login:
    print("entrar no programa")


#logica ou (or)

logica_ou = False or False or True
print(logica_ou)


#operador de negação (not)

negacao = not False

print(negacao)

if not verifica_login:
    print("loga certo ai...")