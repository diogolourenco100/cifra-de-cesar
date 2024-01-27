import os
import platform

def clear():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls')  # Para o Windows
    elif sistema_operacional == 'Linux':
        os.system('clear')  # Para o Linux

def cdc():
    print("")
    print("")
    print("")
    print("        ___   __      ____                          ")
    print("      /      |   \   /                              ")
    print("     (       |    ) (                      by 0xDAM ")
    print("     (       |    ) (                               ")
    print("      \____  |__ /   \____                          ")
    print("")
    print("")
    print("")

def cifra_de_cesar(frase, valor, modo):
    resultado = ""
    for char in frase:
        if char.isalpha():
            if char.islower():
                if modo == 'codificar':
                    resultado += chr((ord(char) - ord('a') + int(valor)) % 26 + ord('a'))
                elif modo == 'decodificar':
                    resultado += chr((ord(char) - ord('a') - int(valor)) % 26 + ord('a'))
            elif char.isupper():
                if modo == 'codificar':
                    resultado += chr((ord(char) - ord('A') + int(valor)) % 26 + ord('A'))
                elif modo == 'decodificar':
                    resultado += chr((ord(char) - ord('A') - int(valor)) % 26 + ord('A'))
        else:
            resultado += char
    return resultado

def decodificar_escolher_valor(frase):
    clear()
    cdc()
    print("Frase Original: ", frase)
    valor = input("\nDigite o valor de deslocamento para decodificação: ")
    resultado = cifra_de_cesar(frase, valor, 'decodificar')
    clear()
    cdc()
    print(f"FRASE ORIGINAL:            {frase}")
    print()
    print(f"FRASE DECODIFICADA PARA {valor}: {resultado}")
    print("\n--------------------------------------------------------------------------------------------------------------")
    input("\nPressione Enter para continuar...")

def decodificar_escolher_range(frase):
    clear()
    cdc()
    print("FRASE ORIGINAL: ", frase)
    inicio = int(input("\nDigite o valor inicial do range: "))
    fim = int(input("Digite o valor final do range: "))
    
    print("\nDecodificação para valores de deslocamento no range:")
    for valor in range(inicio, fim + 1):
        resultado = cifra_de_cesar(frase, valor, 'decodificar')
        print(f"Valor {valor}: {resultado}")
        print()
    
    input("\nPressione Enter para continuar...")

def decodificar_todos_valores(frase):
    clear()
    cdc()
    print("FRASE ORIGINAL: ", frase)
    print("\nDecodificação para valores de deslocamento de 1 a 26:")
    for valor in range(1, 27):
        resultado = cifra_de_cesar(frase, valor, 'decodificar')
        print(f"Valor {valor}: {resultado}")
        print()

    input("\nPressione Enter para continuar...")

def menu():
    clear()
    cdc()
    print("1. Codificar")
    print("2. Decodificar")
    print("3. Sair")
    print()
    print("Escolha uma opção [1][2][3]: ")
    opcao = input("$ ")
    return opcao

def main():
    while True:
        escolha = menu()

        if escolha == '1':
            clear()
            cdc()
            print("Digite a frase para codificá-la: ")
            frase = input("$ ")
            print()
            print("Valor do deslocamento: ")
            valor = input("$ ")
            resultado = cifra_de_cesar(frase, valor, 'codificar')
            clear()
            cdc()
            print("FRASE ORIGINAL: ", frase)
            print()
            print("FRASE DECODIFICADA: ", resultado)
            print("--------------------------------------------------------------------------------------------------------------")
            input("Pressione Enter para continuar...")
        elif escolha == '2':
            clear()
            cdc()
            print("Digite a frase para decodificá-la: ")
            frase = input("$ ")
            print("\n--------------------------------------------------------------------------------------------------------------")
            print("\nOpções de decodificação:")
            print()
            print("1. Escolher um valor específico")
            print("2. Escolher um intervalo (range)")
            print("3. Decodificar para todos os valores de 1 a 26")
            print()
            print("Escolha uma opção [1][2][3]: ")
            opcao_decodificar = input("$ ")
            
            if opcao_decodificar == '1':
                decodificar_escolher_valor(frase)
            elif opcao_decodificar == '2':
                decodificar_escolher_range(frase)
            elif opcao_decodificar == '3':
                decodificar_todos_valores(frase)
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == '3':
            clear()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
