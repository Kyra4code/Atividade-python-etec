from calculos import Somar, Subtrair, Multiplicar, Dividir

def main():
    while True:
        print("\n Insira um valor aritimético para selecionar uma operação: \n")
        x = input("+ para Somar; - para subtrair; x para multiplicar; / para dividir. \n")
        if x == "+":
            Somar()
        else:
            if x == "-":
                Subtrair()
            else: 
                if x == "*":
                    Multiplicar()
                else:
                    if x == "/":
                        Dividir()
                    else:
                        SystemExit()
                        print("\n Error ao entender. \n ")
                        break

    # continue:
    #     print("Error ao entender, tente novamente.")
    #     main()*/

main()