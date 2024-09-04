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
        SystemExit()
    except:
        print("Error ao calcular, tente novamente\n")
        Subtrair()

def Multiplicar():
    try:
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))
        resultado = x * y
        print(f"{resultado}")
        SystemExit()
    except:
        print("Error ao calcular, tente novamente")
        Multiplicar()

def Dividir():
    try:    
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))
        resultado = x / y
        print(f"{resultado}")
        SystemExit()
    except:
        print("Error ao calcular, tente novamente")
        Dividir()