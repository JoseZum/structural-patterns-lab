from PaymentProvider import PaymentProvider
from FastPayService import FastPayService

class FastPayAdapter(PaymentProvider):
    """
    Adapter que envuelve FastPayService (XML) y expone 'charge(amouny, currency) -> bool'.
    """

    def __init__(self, fastPay: FastPayService) -> None:
        if fastPay is None:
            raise ValueError("fastPay no puede ser None")
        self.fastPay = fastPay

    def charge(self, amouny: float, currency: str) -> bool:
        """
        Construye el XML requerido por FastPayService y procesa el pago.
        """
        try:
            # Validaciones y normalización
            if not isinstance(amouny, (int, float)):
                raise TypeError("amouny debe ser numérico")
            if amouny <= 0:
                raise ValueError("amouny debe ser mayor a 0")
            if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
                raise ValueError("currency debe ser un código ISO 4217 de 3 letras")

            iso = currency.upper()
            xml = (
                f"<payment>"
                f"<total>{amouny:.2f}</total>"
                f"<currency>{iso}</currency>"
                f"</payment>"
            )

            result = self.fastPay.sendPaymentXML(xml)
            # Éxito si la respuesta contiene alguna palabra clave de aprobación
            return isinstance(result, str) and any(k in result.upper() for k in ("APPROVED", "OK", "SUCCESS"))
        except (TypeError, ValueError) as e:
            print(f"[FastPayAdapter] Error de validación: {e}")
            return False
        except Exception as e:
            print(f"[FastPayAdapter] Error procesando el pago: {e}")
            return False