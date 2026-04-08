import time as time

print("Bienvenido a una calculadora.\n")

while(True):
    
    salida = input("Si desea salir, porfavor escriba: SALIR\n")
    salida = salida.upper()
    if (salida != "SALIR"):
        numero = float(input(f"\nIngrese un numero para su calculo.\n"))
        operacion = input(f"\nQue desea hacer con ese numero? ({numero}) \n 1.[+]  2.[-]\n")
        if(operacion == "1"):
            operacion = "suma"
        elif(operacion == "2"):
            operacion = "resta"
        numero2 = float(input(f"\nIngrese un segundo numero para poder hacer la {operacion}\n"))
        if (operacion == "suma"):
            resultado = numero + numero2
        elif (operacion == "resta"):
            resultado = numero - numero2
        print(f"Su resultado es: {resultado}")
        time.sleep(3)
        print("\n"*100)    

    
    if (salida == "SALIR"):
        time.sleep(1)    
        break
        


    
 