import time
from sys import stdout

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
#Raices
print(Red+"""
    
                   _ _     _           _         __                  _                       
  __ _ _ __   __ _| (_)___(_)___    __| | ___   / _|_   _ _ __   ___(_) ___  _ __   ___  ___ 
 / _` | '_ \ / _` | | / __| / __|  / _` |/ _ \ | |_| | | | '_ \ / __| |/ _ \| '_ \ / _ \/ __|
| (_| | | | | (_| | | \__ \ \__ \ | (_| |  __/ |  _| |_| | | | | (__| | (_) | | | |  __/\__ \

 \__,_|_| |_|\__,_|_|_|___/_|___/  \__,_|\___| |_|  \__,_|_| |_|\___|_|\___/|_| |_|\___||___/
                                                                                             
Coded by Thiagous
"""+Reset)
print("La grafica tiene raices reales?\n1=Si\n2=No")
opc = input("Opcion = ")
if opc == "1":
    try:
        print(Blue+"Pon las raices")
        global x1
        global x2
        x1 = int(input("Raiz X1 = "))
        x2 = int(input("Raiz X2 = "))
    except ValueError:
        print("Pon numeros enteros")
elif opc == "2":
    print("No tiene raices reales")
else:
    print("Pone 1=Si o 2=No")
    exit()
#Vertices
try:
    print(Blue+"Pon las vertices ")
    v1 = int(input("Vertice Xv = "))
    v2 = int(input("Vertice Yv = "))
except ValueError:
    print("Pon numeros enteros")
#Calculo 
time.sleep(1)
for i in range(101):
        time.sleep(0.01)
        stdout.write("\r[+] Calculando... %d%%" % i)
        stdout.flush()
time.sleep(1)
print("\nDominio: ( - ∞; + ∞)")
#Imagen
if opc == "1":
    if v2 > 0:
        print(f"Imagen: (- ∞;{v2})")
    else:
        print(f"Imagen: ({v2};+ ∞)")
else:
    if v2 < 0:
        print(f"Imagen: (- ∞;{v2})")
    else:
        print(f"Imagen: ({v2};+ ∞)")

#Crecimiento
if opc == "1":
    if v2 > 0:
        print(f"Crecimiento : (- ∞;{v1})")
    else:
        print(f"Crecimiento : ({v1};+ ∞)")
else:
    if v2 < 0:
        print(f"Crecimiento : (- ∞;{v1})")
    else:
        print(f"Crecimiento : ({v1};+ ∞)")
#Decrecimiento
if opc == "1":
    if v2 > 0:
        print(f"Decrecimiento : ({v1};+ ∞)")
    else:
        print(f"Decrecimiento : (- ∞;{v1})")
else:
    if v2 < 0:
        print(f"Decrecimiento : ({v1};+ ∞)")
    else:
        print(f"Decrecimiento : (- ∞;{v1})")  
#C+
if opc == "1":
    if v2 > 0:
        print(f"C+ : ({x1};{x2})")
    else:
        print(f"C+ : (- ∞;{x1}) U ({x2};+ ∞)")
else:
    print("C+ : (- ∞;+ ∞)")
#C-
if opc == "1":
    if v2 > 0:
        print(f"C- : (- ∞;{x1}) U ({x2};+ ∞)")
    else:
        print(f"C- : ({x1};{x2})")
else:
    print("C- : ∉")
#Punto maximo
if v2 < 0:
    print(f"Punto Minimo:({v1};{v2})")
else:
    print(f"Punto Maximo:({v1};{v2})")

