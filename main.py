import time as time
import customtkinter as ctk

#capaz añadir math???? y así hacer una calculadora bien.
#TODO; Aprender a hacer funciones la concha de la gorra (básicamente aprehender python otra vez)

resultado = ''
ventana = ctk.CTk()
ventana.geometry("675x500")

fuente = ctk.CTkFont(
    family = "Roboto",
    size= 16,
    slant= "italic"
)

#UI - Texto de Nombre
intro = ctk.CTkLabel(ventana,text="redmunn's CALCULAT0R.", font= fuente, fg_color="teal",corner_radius=12)
intro.grid(row=0,column=0,padx=20,pady=20)

#UI - Ventana de Resultado
result_wind = ctk.CTkFrame(ventana,width=350,height=50,fg_color="#445a14",corner_radius=12)
result_wind.grid(row=1,column=0,pady=20,padx=20)
result_wind.pack_propagate(False) #Hace que no se ajuste a cualquier texto que tenga dentro
result_text = ctk.CTkLabel(result_wind,text=f"{resultado}",font=fuente,fg_color="transparent", text_color= "white")
result_text.pack(anchor ="w",padx = 10,pady=5) #anchor = "WEST", hace que el texto esté posicionado hacia la izquierda

#entradas de los números
entry_num1= ctk.CTkEntry(ventana,placeholder_text="Ingrese un 1er numero:")
entry_num1.grid(row= 2,column=0,padx=10,pady =10)

entry_num2= ctk.CTkEntry(ventana,placeholder_text="Ingrese un 2do numero:")
entry_num2.grid(row=2,column=1,padx=10,pady=10)
 
#funciones para calculos
def suma():
    resultado = float(entry_num1.get())+float(entry_num2.get())
    result_text.configure(text=str(resultado))
def resta():
    resultado = float(entry_num1.get())-float(entry_num2.get())
    result_text.configure(text=str(resultado))

#botones para cálculos

#suma
botonsuma = ctk.CTkButton(ventana,text="+", command=suma).grid(row=3,column=0,padx=10,pady=10)
#resta
botonresta =ctk.CTkButton(ventana,text="-",command=resta).grid(row=3,column=1,padx=10,pady=10)

ventana.mainloop()


    
 