from traceback import print_tb
import aritmetica as t
import text as a

print(a.Title("Este ","programa ","realiza ","operaciones ","matematicas."))

print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Numero PI")
print("6.Numero PHI o Aureo")
print("7.Costante Gravitacional")

opc=int(input("Escoge un numero: "))
if opc == 1:
   print(a.concat("Suma ","de ","Numeros"))
   print(t.sumDosNum(2,3))

elif opc == 2:

    print(a.concat1("Resta ","de ","Numeros"))
    print(t.resDosNum(2,3))

elif opc == 3:

    print(a.concat2("Multiplicacion ","de ","Numeros"))
    print(t.multDosNum(2,3))

elif opc == 4:

   print(a.concat3("Division ","de ","Numeros"))
   print(t.divDosNum(2,3))

elif opc == 5:
   print(a.concat4("Este ","el "," Numero"," Pi"))
   print(t.NumPI)
elif opc == 6:
    print(a.concat5("Este "," es "," el"," Numero"," Aureo"))
    print(t.NumPHI("--"))
elif opc == 7:
    print(a.concat6("Esta "," es "," la"," constante"," de"," Gravedad"))
    print(t.NumGrav("--"))
else:
    print("Opcion no valida")

