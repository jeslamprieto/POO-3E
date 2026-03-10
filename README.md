# POO-3E - Taller: Clases y Objetos 🐍

Taller práctico de **Programación Orientada a Objetos (POO)** en Python. Cada ejercicio implementa una clase con atributos y métodos que modelan objetos del mundo real.

---

## 📁 Contenido

### Ejercicio1.py — Clase `libro`
Modela un libro con título, autor y número de páginas.

**Métodos:**
- `mostrar_info()` → Muestra los datos del libro
- `actualizar_paginas(nuevo_numero)` → Actualiza el número de páginas

**Funcionalidad:** Crea dos libros y permite al usuario actualizar las páginas de uno de ellos de forma interactiva.

---

### Ejercicio2.py — Clase `estudiante`
Modela un estudiante con nombre, apellido, edad y calificación.

**Métodos:**
- `mostrar_info()` → Muestra los datos del estudiante
- `clasificacion()` → Indica si el estudiante está **Aprobado** (≥ 3.0) o **Reprobado**

**Funcionalidad:** Crea dos estudiantes y muestra su información junto con su estado académico.

---

### Ejercicio3.py — Clase `producto`
Modela un producto de inventario con nombre, precio y stock.

**Métodos:**
- `verificar_disponibilidad(cantidad)` → Verifica si hay stock suficiente
- `vender(cantidad)` → Descuenta unidades del stock si hay disponibilidad
- `reabastecer(cantidad)` → Aumenta el stock del producto

**Funcionalidad:** Simula operaciones de una tienda con una laptop como producto de prueba.

---

### Ejercicio4.py — Clase `vehiculo`
Modela un vehículo con marca, modelo y velocidad máxima.

**Métodos:**
- `acelerar(incremento)` → Aumenta la velocidad sin superar el límite máximo
- `frenar(decremento)` → Reduce la velocidad sin bajar de 0
- `verificar_limite()` → Indica si la velocidad actual está dentro del límite

**Funcionalidad:** Menú interactivo para controlar un Toyota Corolla (210 km/h máx).

---

## ▶️ Requisitos

- Python 3.x

## 🚀 Ejecución

```bash
python Ejercicio1.py
python Ejercicio2.py
python Ejercicio3.py
python Ejercicio4.py
```

---

## 👤 Autor

**Jeslam Prieto**  
Curso: Programación Orientada a Objetos — 3E
