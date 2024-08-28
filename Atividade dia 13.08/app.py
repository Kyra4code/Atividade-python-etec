def main():
    try:
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
                        print("\n Error ao entender, tente novamente \n ")
    
    except:
        print("Error ao entender, tente novamente.")
        main()

def Somar():
    try:
        x = int(input("Primeiro valor: "))
        y = int(input("Segundo valor: "))
        resultado = x + y
        print(f"{resultado}")
    except:
        print("Error ao calcular, tente novamente\n")
        Somar()

def Subtrair():
    try:
        x = int(input("Primeiro valor: "))
        y = int(input("Segundo valor: "))
        resultado = x - y
        print(f"{resultado}")
    except:
        print("Error ao calcular, tente novamente\n")
        Subtrair()

def Multiplicar():
    try:
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))
        resultado = x * y
        print(f"{resultado}")
    except:
        print("Error ao calcular, tente novamente")
        Multiplicar()

def Dividir():
    try:    
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))
        resultado = x / y
        print(f"{resultado}")
    except:
        print("Error ao calcular, tente novamente")
        Dividir()

main()