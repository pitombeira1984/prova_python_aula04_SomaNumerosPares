def SomarNumerosPares():
    soma_numeros_pares = 0
    principio = int(input("Digite o número que representa o princípio do intervalo: "))
    fim = int(input("Digite o número que representa o fim do intervalo: "))
    
    for numero in range(principio, fim + 1):
        if numero % 2 == 0:
             soma_numeros_pares += numero
    
    if soma_numeros_pares == 0:
        print("Não há números pares no intervalo.")
    else:
        print(f"Soma dos Números Pares: {soma_numeros_pares}")

SomarNumerosPares()
