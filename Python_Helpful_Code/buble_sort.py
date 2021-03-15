def enbuyukbulma(liste):
    eldetutulan = liste[0]
    for i in liste:
        if i > eldetutulan:
            eldetutulan = i
    return eldetutulan
    


def sort(liste):
    k = len(liste)
    liste_1 = []
    while True:
        n = enbuyukbulma(liste)
        liste_1.append(n)
        liste.remove(n)
        if len(liste_1) == k:
            return liste_1
            


liste = []
x = int(input("kaç sayı gireceğinizi giriniz:"))
for i in range(0,x):
    p = int(input())
    liste.append(p)
    

print(sort(liste))
        
            
