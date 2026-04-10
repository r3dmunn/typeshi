import time as time
import customtkinter as ctk
#capaz añadir math???? y así hacer una calculadora bien.
#TODO; Aprender a hacer funciones la concha de la gorra (básicamente aprehender python otra vez)

def suma(x,y):  #es por acá, tengo q definir funciones así no se coje todo el coso #TODO; Definir funciones en otro archivo así se libera de código acá, y los llamo
    x + y       #Igual las funciones me da none
def resta(x,y):
    x - y

ventana = ctk.CTk()
ventana.geometry("400x550")

fuente = ctk.CTkFont(
    family = "Roboto",
    size= 16,
    slant= "italic"
)

intro = ctk.CTkLabel(ventana,text="redmunn's CALCULAT0R.", font= fuente, fg_color="teal",corner_radius=12)
intro.pack(padx= 20,pady= 20)



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
            resultado = suma(numero,numero2) #otro que me da None
        elif (operacion == "resta"):
            resultado = resta(numero,numero2) #me da None(????)
        print(f"Su resultado es: {resultado}")
        time.sleep(3)
        print("\n"*100)



    
    if (salida == "SALIR"):
        break

result_window = ctk.CTkLabel(ventana,text=f"{resultado}",font= fuente,fg_color="#445a14", corner_radius=12) #Se ve como la mierda, tengo que hacer un cuadrado atrás para que pareciese la pantalla de una calculadora real
result_window.pack(padx= 20, pady= 20)

ventana.mainloop()


    
 