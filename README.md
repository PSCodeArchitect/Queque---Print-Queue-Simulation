# Simulador de Cola de Impresión
## Descripción del proyecto

Este proyecto consiste en una simulación de una cola de impresión utilizando estructuras de datos en Python. 
El sistema representa cómo una impresora recibe distintos documentos, los almacena en una cola de espera y los procesa uno por uno siguiendo el orden de llegada.
La aplicación fue desarrollada utilizando una interfaz gráfica con Tkinter y permite visualizar en tiempo real el funcionamiento de la impresora, 
el estado de la cola y estadísticas de rendimiento.

---

# Características principales

* Implementación manual de una estructura Queue (cola)
* Simulación de impresión documento por documento
* Procesamiento FIFO (First In, First Out)
* Interfaz gráfica en Tkinter
* Validación de datos ingresados
* Estadísticas automáticas
* Cambio dinámico de colores según el estado de la impresora

---

# Clases implementadas

## Queue

Clase encargada de administrar la cola de impresión.

Funciones principales:

* enqueue()
* dequeue()
* is_empty()
* size()

La cola trabaja con el principio FIFO:
el primer documento en entrar es el primero en imprimirse.

---

## PrintTask

Representa cada documento de impresión.

Contiene:

* nombre del documento
* cantidad de páginas
* tiempo de llegada
* tiempo de inicio de impresión

También calcula el tiempo de espera del documento.

---

## Printer

Simula el funcionamiento de la impresora.

Se encarga de:

* tomar el siguiente trabajo
* imprimir página por página
* indicar si está libre u ocupada
* controlar el documento actual

---

# Funcionamiento de la simulación

1. El usuario agrega documentos desde la interfaz gráfica.
2. Los documentos ingresan a una cola de espera.
3. La impresora toma el primer documento disponible.
4. El sistema imprime una página por ciclo de simulación.
5. Cuando un trabajo termina, la impresora toma el siguiente documento.
6. Se actualizan automáticamente las estadísticas.

---

# Interfaz gráfica

La ventana está dividida en cuatro cuadros principales:

## Cuadro 1

Ingreso de documentos:

* nombre
* cantidad de páginas

## Cuadro 2

Visualización de la cola de impresión y botón para iniciar la simulación.

## Cuadro 3

Estado de la impresora en tiempo real.

Colores:

* Verde → impresora libre
* Rojo → imprimiendo documentos

## Cuadro 4

Muestra estadísticas de la simulación.

---

# Métricas calculadas

El sistema calcula:

* cantidad total de trabajos procesados
* tiempo promedio de espera
* documento con mayor tiempo de espera
* tamaño máximo alcanzado por la cola

---

# Validaciones implementadas

El sistema valida:

* documentos con páginas menores o iguales a cero
* entradas vacías
* errores de conversión de datos
* simulación sin documentos

---

# Pruebas mínimas
Se realizaron pruebas para verificar:
* funcionamiento correcto de Queue
* comportamiento FIFO
* procesamiento correcto de trabajos
* cálculo básico de métricas

---
# Requisitos
* Python 3
* Importar Tkinter
---
# Cómo ejecutar
1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar el archivo principal:
