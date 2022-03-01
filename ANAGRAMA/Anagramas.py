
print("VERIFICADOR DE ANAGRAMAS")
var1=input("Ingrese la primera palabra")
var2=input("Ingrese la segunda  palabra")

a=0
y=0
for i in var1:
    a=a+1
    for j in var2:
        if i == j:
            y=y+1
            if a<y:
                y=y-1


if y == len(var1):
    print("Si son Anagramas")
else:
    print ("No son Anagrama")