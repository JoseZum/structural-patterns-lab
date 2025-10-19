from PaymentProvider import PaymentProvider
from typing import Any

class PayLinkAdapter(PaymentProvider):
    """
    Adapter para PayLinkAPI que expone una interfaz con 'charge(...) : bool'.
    - Acepta un objeto PayLinkAPI en el constructor.
    - Retorna True si el cargo fue exitoso; False si hubo error de validación u otra excepción esperada.
    """
    #Constructor
    def __init__(self, payLink: Any) -> None:
        """
        Args:
            payLink: Instancia de PayLinkAPI.
        """
        if payLink is None:
            raise ValueError("payLink no puede ser None")
        self.payLink = payLink  # tipo: PayLinkAPI

    #logica del metodo charge para hacer un cargo
    def charge(self, amouny: float, currency: str) -> bool:
        """
        Realiza un cargo usando PayLinkAPI.makePayment(total, isoCurrency).

        Args:
            amouny (float): Monto a cobrar.
            currency (str): Código ISO 4217, por ejemplo 'USD' o 'CRC'.

        Returns:
            bool: True si el pago fue procesado; False si hubo error de parámetros u otra falla controlada.
        """
        try:
            # delega al método de la API; este lanza excepciones si hay parámetros inválidos.
            self.payLink.makePayment(amouny, currency)
            return True
        except (TypeError, ValueError) as e:
            # Errores de validación: devolvemos False en lugar de propagar.
            print(f"[PayLinkAdapter] Error de validación: {e}")
            return False
        except Exception as e:
            # Cualquier otro error controlado.
            print(f"[PayLinkAdapter] Error procesando el pago: {e}")
            return False