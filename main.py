
def main():
    n1 = int(input("Introdueix el primer enter: "))
    n2: int = int(input("Introdueix el segon enter: "))
    if n1 < n2:
        while n1 < n2+1:
            print(n1)
            n1+=1
    else:
        while n1 > n2:
            print("Error")
            n1 = int(input("Introdueix el primer enter: "))
            n2 = int(input("Introdueix el segon enter: "))
            aux = n1
        while aux < n2 + 1:
            print(aux)
            aux += 1

if __name__ == '__main__':
    main()
