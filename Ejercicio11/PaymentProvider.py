from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    """
    Interfaz de proveedor de pagos.
    Implementaciones deben exponer 'charge(amouny, currency) -> bool'.
    """
    #interfaz del metodo charge para ser implementado en las clases hijas
    @abstractmethod
    def charge(self, amouny: float, currency: str) -> bool:
        """
        Procesa un cargo.

        Args:
            amouny (float): Monto a cobrar.
            currency (str): Código ISO 4217 de 3 letras.

        Returns:
            bool: True si el cargo fue exitoso; False en caso contrario.
        """
        raise NotImplementedError