def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

nota = 7
if nota <6:
    print(f"Sua nota é: {nota}")
    print("reprovado")

else:
    print("aprovado")


print("Fim")

nota_final = 5

if nota_final < 4:
    print("reprovado")
else:
    nota = 7
    if nota_final < 6:
        print(f"Sua nota final é: {nota_final}")
        print("recuperação")

    else:
        print("aprovado")

print("Fim")