import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# ------------------- Ventana -------------------
root = tk.Tk()
root.title("Traductor JMP")
root.geometry("800x650")
root.resizable(False, False)

# ------------------- VARIABLES -------------------
tema_actual = "light"

idiomas = [
    "spanish", "english", "french", "german", "italian",
    "portuguese", "russian", "japanese", "chinese", "korean",
    "arabic", "hindi"
]

colores = {
    "light": {
        "texto": "#000000",
        "entrada_bg": "white",
        "entrada_texto": "black",
        "boton_bg": "#4CAF50",
        "boton_texto": "white",
        "panel_bg": "#FFFFFF",
    },
    "dark": {
        "texto": "#e6e6e6",
        "entrada_bg": "#3a3a3a",
        "entrada_texto": "white",
        "boton_bg": "#009688",
        "boton_texto": "white",
        "panel_bg": "#000000",
    }
}

# ------------------- FUNCIONES -------------------
def aplicar_tema():
    c = colores[tema_actual]

    root.configure(bg=c["panel_bg"])
    panel.config(bg=c["panel_bg"])

    titulo.config(bg=c["panel_bg"], fg=c["texto"])
    label_trad.config(bg=c["panel_bg"], fg=c["texto"])
    label_de.config(bg=c["panel_bg"], fg=c["texto"])
    label_a.config(bg=c["panel_bg"], fg=c["texto"])

    entrada.config(bg=c["entrada_bg"], fg=c["entrada_texto"])
    salida.config(bg=c["entrada_bg"], fg=c["entrada_texto"])

    style.configure("TCombobox",
                    fieldbackground=c["entrada_bg"],
                    background=c["entrada_bg"],
                    foreground=c["entrada_texto"],
                    arrowcolor=c["entrada_texto"])

    style.configure("TButton",
                    background=c["boton_bg"],
                    foreground=c["boton_texto"],
                    relief="flat")

    boton_traducir.config(style="TButton")
    boton_tema.config(style="TButton")


def traducir():
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, "No hay texto para traducir.")
        return

    src = combo_origen.get()
    dest = combo_destino.get()

    try:
        traduccion = GoogleTranslator(source=src, target=dest).translate(texto)
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, traduccion)
    except Exception as e:
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, f"Error: {e}")


def cambiar_tema():
    global tema_actual
    tema_actual = "dark" if tema_actual == "light" else "light"
    aplicar_tema()


# ------------------- ESTILO -------------------
style = ttk.Style()
style.theme_use('default')

# ------------------- TITULO -------------------
titulo = tk.Label(root, text="Traductor Multilenguaje JMP ⚡",
                  font=("Segoe UI", 18, "bold"))
titulo.pack(pady=10)

# ------------------- PANEL PRINCIPAL -------------------
panel = tk.Frame(root, bd=0)
panel.place(relx=0.5, rely=0.5, anchor="center", width=700, height=440)

# ------------------- IDIOMAS -------------------
frame_idiomas = tk.Frame(panel, bg=colores[tema_actual]["panel_bg"])
frame_idiomas.pack(pady=5)

label_de = tk.Label(frame_idiomas, text="De:", font=("Segoe UI", 11, "bold"))
label_de.grid(row=0, column=0, padx=5)

combo_origen = ttk.Combobox(frame_idiomas, values=idiomas, width=20)
combo_origen.set("spanish")
combo_origen.grid(row=0, column=1)

label_a = tk.Label(frame_idiomas, text="A:", font=("Segoe UI", 11, "bold"))
label_a.grid(row=0, column=2, padx=5)

combo_destino = ttk.Combobox(frame_idiomas, values=idiomas, width=20)
combo_destino.set("english")
combo_destino.grid(row=0, column=3)

# ------------------- ENTRADA -------------------
entrada = tk.Text(panel, height=5, width=70, font=("Segoe UI", 11))
entrada.pack(pady=5)

# ------------------- BOTON TRADUCIR -------------------
boton_traducir = ttk.Button(panel, text="Traducir", command=traducir)
boton_traducir.pack(pady=15)

# ------------------- SALIDA -------------------
label_trad = tk.Label(panel, text="Traducción:", font=("Segoe UI", 12, "bold"))
label_trad.pack()

salida = tk.Text(panel, height=6, width=70, font=("Segoe UI", 11))
salida.pack()

# ------------------- BOTÓN CAMBIAR TEMA -------------------
boton_tema = ttk.Button(root, text="Cambiar tema (Light/Dark)", command=cambiar_tema)
boton_tema.place(x=10, y=10)

# ------------------- INICIALIZAR -------------------
aplicar_tema()  # Aplica el tema inicial

# ------------------- INICIAR LA INTERFAZ -------------------
root.mainloop()
