from tkinter import messagebox
import tkinter as tk
import openai

# Configurar la API de OpenAI con tu clave de API
openai.api_key = "Your_API_Key"

# Función para enviar la pregunta a OpenAI y mostrar la respuesta en una ventana de mensaje
def enviar_pregunta():
    prompt = entrada_pregunta.get()
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048,
        )
        messagebox.showinfo("Respuesta", respuesta.choices[0].text)
    except Exception as e:
        messagebox.showerror("Error", e)

# Crear la ventana y agregar los componentes de la interfaz de usuario
ventana = tk.Tk()
ventana.title("OpenAI Preguntas y Respuestas")

label_pregunta = tk.Label(ventana, text="Pregunta:")
label_pregunta.pack()

entrada_pregunta = tk.Entry(ventana)
entrada_pregunta.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_pregunta)
boton_enviar.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
