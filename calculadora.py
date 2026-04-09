import time as time
import customtkinter as ctk

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
    ventana.mainloop()
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
        break
        


    
 