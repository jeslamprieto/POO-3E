# SEMANA 9 - Clases Abstractas en POO

Ejercicios prácticos sobre el concepto de Clases Abstractas en Programación Orientada a Objetos usando Python.

---

## Ejercicio 1 - Sistema de Notificaciones

Clases: `Notificacion` (abstracta), `EmailNotificacion` y `SMSNotificacion` (subclases)

- `Notificacion` define el método abstracto `enviar()`
- `EmailNotificacion` implementa `enviar()` con asunto y cuerpo del mensaje
- `SMSNotificacion` implementa `enviar()` con un límite de 160 caracteres

---

## Ejercicio 2 - Sistema de Medición de Temperatura

Clases: `SensorTemperatura` (abstracta), `SensorCelsius` y `SensorFahrenheit` (subclases)

- `SensorTemperatura` define el método abstracto `obtener_temperatura()`
- `SensorCelsius` obtiene la temperatura en Celsius y puede convertirla a Fahrenheit
- `SensorFahrenheit` obtiene la temperatura en Fahrenheit y puede convertirla a Celsius

---

## Ejercicio 3 - Sistema de Pago

Clases: `MetodoPago` (abstracta), `TarjetaCredito` y `Paypal` (subclases)

- `MetodoPago` define el método abstracto `procesar_pago(monto)`
- `TarjetaCredito` valida el número de tarjeta y código de seguridad antes de procesar el pago
- `Paypal` verifica que el saldo sea suficiente antes de completar la transacción
- Manejo de excepciones con `try/except` para errores de validación

---

## Conceptos aplicados

- Clases abstractas con `from abc import ABC, abstractmethod`
- Métodos abstractos con `@abstractmethod`
- Subclases que implementan los métodos abstractos
- Manejo de excepciones con `raise ValueError` y `try/except`