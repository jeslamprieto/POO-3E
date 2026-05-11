
from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass



class EmailNotificacion(Notificacion):
    def __init__(self, destinatario, asunto, cuerpo):
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

    def enviar(self):
        print(f"Enviando Email a: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Cuerpo: {self.cuerpo}")

class SMSNotificacion(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        if len(mensaje) > 160:
            raise ValueError("El mensaje supera el limite de 160 caracteres.")
        self.mensaje = mensaje

    def enviar(self):
        print(f"Enviando SMS al numero: {self.numero}")
        print(f"Mensaje: {self.mensaje}")

email = EmailNotificacion("pepito@gmail.com", "Bienvenido", "Hola Pepito, bienvenido al sistema.")
sms = SMSNotificacion("3001234567", "Tu codigo de verificacion es 1234.")

email.enviar()
print("---")
sms.enviar()
