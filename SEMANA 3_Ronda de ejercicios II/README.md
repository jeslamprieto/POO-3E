# POO-3E - Semana 3: Ronda de Ejercicios II 🐍

Ronda de ejercicios de **Programación Orientada a Objetos (POO)** en Python, enfocada en **encapsulamiento, herencia y métodos especiales**.

---

## 📁 Contenido

### Ejercicio1.py — Clase `Producto`
Modela un producto con nombre y precio usando **encapsulamiento** (atributos privados).

**Métodos:**
- `get_nombre()` / `get_precio()` → Obtienen los atributos privados
- `set_precio(nuevo_precio)` → Actualiza el precio validando que sea mayor a 0
- `aplicar_descuento(porcentaje)` → Aplica un descuento entre 0 y 100%

---

### Ejercicio2.py — Clase `Rectangulo`
Modela un rectángulo con largo y ancho privados.

**Métodos:**
- `get_dimensiones()` → Muestra las dimensiones actuales
- `set_dimensiones(largo, ancho)` → Actualiza las dimensiones validando que sean positivas
- `calcular_area()` → Retorna el área (largo × ancho)
- `calcular_perimetro()` → Retorna el perímetro (2 × (largo + ancho))

---

### Ejercicio3.py — Clase `Estudiante`
Modela un estudiante con nombre, edad y lista de notas privadas.

**Métodos:**
- `get_nombre()` / `get_edad()` → Obtienen los atributos privados
- `agregar_nota(nota)` → Agrega una nota validando que esté entre 0 y 100
- `calcular_promedio()` → Calcula el promedio de todas las notas

---

### Ejercicio4.py — Clase `Libro`
Modela un libro con seguimiento de página actual usando atributos privados.

**Métodos:**
- `get_info()` → Muestra toda la información del libro
- `get_pagina_actual()` → Retorna la página en la que se encuentra
- `avanzar_paginas(num)` → Avanza páginas sin superar el total
- `retroceder_paginas(num)` → Retrocede páginas sin bajar de la página 1

---

### Ejercicio5.py — Clases `CuentaBancaria` y `CuentaAhorro`
Implementa **herencia**: `CuentaAhorro` extiende `CuentaBancaria`.

**CuentaBancaria:**
- `depositar(monto)` → Agrega saldo validando monto positivo
- `retirar(monto)` → Descuenta saldo validando fondos suficientes
- `consultar_saldo()` / `consultar_titular()` → Retornan info de la cuenta

**CuentaAhorro (hereda de CuentaBancaria):**
- `get_interes()` → Retorna el porcentaje de interés anual
- `aplicar_interes()` → Calcula y deposita el interés sobre el saldo actual

---

### Ejercicio6.py — Clase `Empleado`
Usa un **atributo de clase** y un **método de clase** para llevar el conteo de empleados creados.

**Métodos:**
- `cantidad_empleados()` *(classmethod)* → Retorna el total de empleados registrados

---

### Ejercicio7.py — Clase `TarjetaCredito`
Usa un **método estático** para validar tarjetas mediante el **algoritmo de Luhn**.

**Métodos:**
- `validar_tarjeta(numero)` *(staticmethod)* → Retorna `True` si el número de tarjeta es válido

---

## 💡 Conceptos aplicados

- 🔒 **Encapsulamiento** → Atributos privados con `__` y métodos getter/setter
- 🧬 **Herencia** → `CuentaAhorro` extiende `CuentaBancaria`
- 🏷️ **Métodos de clase** → `@classmethod` en `Empleado`
- ⚙️ **Métodos estáticos** → `@staticmethod` en `TarjetaCredito`

---

## ▶️ Requisitos

- Python 3.x

## 🚀 Ejecución

```bash
python Ejercicio1.py
python Ejercicio2.py
python Ejercicio3.py
python Ejercicio4.py
python Ejercicio5.py
python Ejercicio6.py
python Ejercicio7.py
```

---

## 👤 Autor

**Jeslam Prieto**  
Curso: Programación Orientada a Objetos — 3E
