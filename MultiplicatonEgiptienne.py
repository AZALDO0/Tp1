nombre1= int(input("Insérer un nombre :"))
nombre2= int(input("Insérer un nombre2 :"))
def puissance(n): 
    
    x = 0
    y = 0
    
    while (y <= n):

        y = 2**x
        x += 1

    return y//2

def CarreNombre(nombre1,nombre2):
    if nombre1 == 1 and nombre2 == 1:
        return 1

    elif (nombre1 != nombre2 and (nombre1 == 1 or nombre2 == 1)):
        return max(nombre1,nombre2)

    elif nombre1 == 0 or nombre2 == 0:
        return 0

    else:

        a = min(nombre1,nombre2)
        b = max(nombre1,nombre2)
        c = 0
        i = 0
        multi = 0

        d = {}

        while True:

            k = puissance(a)
            i = k
            a = a - i

            while i != 0:
                c += b 
                i -= 1
            d[k] = c
            c = 0
            
            if a == 0:
                
                break
        print(d)
        for key in d.keys():
            multi += d[key]

        return multi

 
print(CarreNombre(nombre1,nombre2))
