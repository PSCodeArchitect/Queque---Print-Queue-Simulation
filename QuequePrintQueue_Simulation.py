import tkinter as tk

# CLASE QUEUE
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# CLASE PRINT TASK
class PrintTask:
    def __init__(self, nombre, paginas, llegada):
        if paginas <= 0:
            raise ValueError("Paginas invalidas")
        self.nombre = nombre
        self.paginas = paginas
        self.llegada = llegada
        self.inicio = None

    def tiempo_espera(self):
        return self.inicio - self.llegada


# =========================
# CLASE PRINTER
# =========================
class Printer:
    def __init__(self):
        self.documento_actual = None
        self.hojas_restantes = 0

    def libre(self):
        return self.documento_actual is None

    def tomar_trabajo(self, trabajo, tiempo_actual):
        self.documento_actual = trabajo
        self.documento_actual.inicio = tiempo_actual
        self.hojas_restantes = trabajo.paginas

    def imprimir_hoja(self):
        if self.documento_actual is not None:
            self.hojas_restantes -= 1

    def terminado(self):
        return self.hojas_restantes <= 0



# VARIABLES GLOBALES
cola_impresion = Queue()
impresora = Printer()
tiempo_actual = 0
trabajos_procesados = 0
suma_esperas = 0
mayor_espera = 0
documento_mayor = ""

max_cola = 0



# FUNCION IMPRIMIR
def imprimir():
    global tiempo_actual
    global trabajos_procesados
    global suma_esperas
    global mayor_espera
    global documento_mayor
    global max_cola

    # SI NO HAY DOCUMENTO ACTUAL
    if impresora.libre():
        trabajo = cola_impresion.dequeue()
        if trabajo is None:
            estado_impresion.config(
                text="No hay documentos", bg="green" )
            cuadro3.config(bg="green")
            return

        lista.delete(0)
        impresora.tomar_trabajo(trabajo, tiempo_actual)

    # COLOR ROJO CUANDO ESTA IMPRIMIENDO EN CUADRO 3
    cuadro3.config(bg="red")
    estado_impresion.config(
        bg="red",
        text=
        f"Imprimiendo:\n"
        f"{impresora.documento_actual.nombre}\n\n"
        f"Hojas restantes: {impresora.hojas_restantes}"
    )

    impresora.imprimir_hoja()
    tiempo_actual += 1
    # SI TERMINO
    if impresora.terminado():
        espera = impresora.documento_actual.tiempo_espera()
        trabajos_procesados += 1
        suma_esperas += espera
        # MAYOR ESPERA
        if espera > mayor_espera:
            mayor_espera = espera
            documento_mayor = impresora.documento_actual.nombre
        promedio = suma_esperas / trabajos_procesados
        estadisticas.config(
            text=
            f"Trabajos procesados: {trabajos_procesados}\n\n"
            f"Promedio espera: {promedio:.2f}\n\n"
            f"Mayor espera: {documento_mayor}\n\n"
            f"Tiempo mayor espera: {mayor_espera}\n\n"
            f"Max cola: {max_cola}"
        )

        estado_impresion.config(
            text=f"{impresora.documento_actual.nombre} terminado"
        )

        impresora.documento_actual = None
        ventana.after(1000, imprimir)
    else:
        ventana.after(700, imprimir)



# AGREGAR DOCUMENTOS
def agregar_documento():
    global tiempo_actual
    global max_cola
    try:

        nombre = in_nombre.get().strip()
        paginas = int(in_paginas.get())
        if nombre == "":
            estado_impresion.config(text="Nombre vacio")
            return

        documento = PrintTask(
            nombre,
            paginas,
            tiempo_actual
        )

        cola_impresion.enqueue(documento)
        # ACTUALIZAR MAX COLA
        if cola_impresion.size() > max_cola:
            max_cola = cola_impresion.size()

        lista.insert(
            tk.END,
            f"{nombre} | {paginas} paginas"
        )

        tiempo_actual += 1
        in_nombre.delete(0, tk.END)
        in_paginas.delete(0, tk.END)

    except ValueError:
        estado_impresion.config(
            text="Datos invalidos"
        )



# PRUEBAS MINIMAS
def pruebas():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    tarea = PrintTask("Doc", 5, 0)
    assert tarea.paginas == 5
    print("Pruebas correctas")


pruebas()



#======================== INTERFAZ================================

ventana = tk.Tk()
ventana.title("SIMULADOR DE IMPRESION")
ventana.geometry("700x500")

# Usamos GRID para definir los cuadrados
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

# FRAMES
cuadro1 = tk.Frame(ventana, bg="lightblue")
cuadro2 = tk.Frame(ventana, bg="white")
cuadro3 = tk.Frame(ventana, bg="green")
cuadro4 = tk.Frame(ventana, bg="lightyellow")

cuadro1.grid(row=0, column=0, sticky="nsew")
cuadro2.grid(row=0, column=1, sticky="nsew")
cuadro3.grid(row=1, column=0, sticky="nsew")
cuadro4.grid(row=1, column=1, sticky="nsew")


#DATOS DEL  CUADRADO 1
tk.Label(
    cuadro1,
    text="Agregar Documento",
    bg="lightblue",
    font=("Arial", 14)
).pack(pady=10)

tk.Label(
    cuadro1,
    text="Nombre:"
).pack()

in_nombre = tk.Entry(cuadro1)
in_nombre.pack()
tk.Label(
    cuadro1,
    text="Paginas:"
).pack()

in_paginas = tk.Entry(cuadro1)
in_paginas.pack()
tk.Button(
    cuadro1,
    text="Agregar",
    command=agregar_documento
).pack(pady=10)



# DATOS PARA EL CUADRADO 2
lista = tk.Listbox(cuadro2)
lista.pack(fill="both", expand=True, padx=10, pady=10)
tk.Button(
    cuadro2,
    text="Iniciar Impresion",
    command=imprimir
).pack(pady=10)


# DATOS PARA EL CUADRADO 3

estado_impresion = tk.Label( cuadro3,  text="Impresora libre",  bg="green",  fg="white",  font=("Arial", 14))
estado_impresion.pack(expand=True)


#DATOS PARA EL  CUADRADO 4

estadisticas = tk.Label(cuadro4,  text="Sin estadisticas",  justify="left",  bg="lightyellow",  font=("Arial", 12))
estadisticas.pack(pady=20)
ventana.mainloop()
