def main():
    x = input("Insira o primeiro valor: ")
    y = input("Insira o segundo valor: ")
    z = input("Insira o terceir valor: ")

    if x > y and z:
        print(f"O primeiro valor inserido {x} é maior")
    elif y > x and z:
        print(f"O segudo valor inserido {y} é maior")
    elif z > x and y:
        print(f"O terceiro numero inserido {z} é maior")
    else:
        print("Existe alguns numeros iguais")

main()