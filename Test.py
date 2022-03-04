


entrer = input("Inserer un nombre Strictement positif :")
list1 = []
nombre= int(entrer)
list1.append(nombre)
def conjSyracus(n):
    for x in range(0,17):        
        evenNot = n % 2        
        if (evenNot==0):
           n= n / 2 
        elif(evenNot!= 0):
            n=(n*3) + 1
                    
        list1.append(int(n))
for x in range(0,3):        
    conjSyracus(nombre)

print(list1)

fichier = open("syracuse.txt", "w")
fichier.write(str(list1))
fichier.close()

def reading(self):
        
    fichier = open("syracuse.txt", "r")
    print(fichier.read())
    fichier.close()

        



        


