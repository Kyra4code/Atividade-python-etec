from datetime import datetime

#instância da função datetime.now()
now = datetime.now()

#para saber o ano atual 
ano_atual = int(now.strftime("%Y"))

def main():
    x = int(input("Qual sua idade? \n"))
    calc = ano_atual - x

    print(f"O ano que você nasceu é {calc}")

main()