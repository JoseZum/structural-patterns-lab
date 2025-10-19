from PaymentProvider import PaymentProvider
from SafeTransferClient import SafeTransferClient

class SafeTransferAdapter(PaymentProvider):
    """
    Adapter para SafeTransferClient que expone 'charge(amouny, currency) -> bool'.
    """
    #constructor
    def __init__(self, safeTransfer: SafeTransferClient) -> None:
        if safeTransfer is None:
            raise ValueError("safeTransfer no puede ser None")
        self.safeTransfer = safeTransfer

    #logica del metodo charge para hacer un cargo
    def charge(self, amouny: float, currency: str) -> bool:
        """
        Convierte los parámetros al formato requerido por SafeTransferClient y procesa el pago.
        """
        try:
            # Validación y normalización
            if not isinstance(amouny, (int, float)):
                raise TypeError("amouny debe ser numérico")
            if amouny <= 0:
                raise ValueError("amouny debe ser mayor a 0")
            if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
                raise ValueError("currency debe ser un código ISO 4217 de 3 letras")

            iso = currency.upper()
            money_str = f"{amouny:.2f}"

            status = self.safeTransfer.makeSecurePay(money_str, iso)
            # Éxito si el servicio devuelve 1 (aprobado)
            return isinstance(status, int) and status == 1
        except (TypeError, ValueError) as e:
            print(f"[SafeTransferAdapter] Error de validación: {e}")
            return False
        except Exception as e:
            print(f"[SafeTransferAdapter] Error procesando el pago: {e}")
            return False