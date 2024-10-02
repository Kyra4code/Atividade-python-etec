lista = ["Banana", "melancia", "abobora"]

def appendInsert():
    print(lista)
    lista.append("amendoim")
    print(lista)
    lista.remove("amendoim")
    lista.insert(3, "amendoim")
    print(lista)
    
appendInsert()


def removeDel():
    print(lista)
    lista.remove("Banana")
    print(lista)
    lista.insert(0, "Banana")
    del(lista[0])
    print(lista)

removeDel()

lista2 = ("um", "dois", "tres")