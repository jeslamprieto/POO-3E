from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


## Clase TarjetaCredito
class TarjetaCredito(MetodoPago):
    def __init__(self, numero_tarjeta, fecha_expiracion, codigo_seguridad):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.codigo_seguridad = codigo_seguridad

    def procesar_pago(self, monto):
        if len(str(self.numero_tarjeta)) != 16:
            raise ValueError("Numero de tarjeta invalido.")
        if len(str(self.codigo_seguridad)) != 3:
            raise ValueError("Codigo de seguridad invalido.")
        print(f"Procesando pago de ${monto} con tarjeta terminada en {str(self.numero_tarjeta)[-4:]}")
        print(f"Pago de ${monto} procesado correctamente.")


## Clase Paypal
class Paypal(MetodoPago):
    def __init__(self, correo_electronico, saldo):
        self.correo_electronico = correo_electronico
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo < monto:
            raise ValueError(f"Saldo insuficiente. Saldo actual: ${self.saldo}")
        self.saldo -= monto
        print(f"Procesando pago de ${monto} con PayPal ({self.correo_electronico})")
        print(f"Pago de ${monto} procesado correctamente. Saldo restante: ${self.saldo}")


## Pruebas
print("--- Pago con Tarjeta de Credito ---")
try:
    tarjeta = TarjetaCredito(4532015112830366, "12/26", 123)
    tarjeta.procesar_pago(500)
except ValueError as e:
    print(f"Error: {e}")

print("")

print("--- Pago con PayPal ---")
try:
    paypal = Paypal("pepito@gmail.com", 1000)
    paypal.procesar_pago(300)
except ValueError as e:
    print(f"Error: {e}")

print("")

print("--- Pago con PayPal con saldo insuficiente ---")
try:
    paypal2 = Paypal("juancho@gmail.com", 100)
    paypal2.procesar_pago(500)
except ValueError as e:
    print(f"Error: {e}")