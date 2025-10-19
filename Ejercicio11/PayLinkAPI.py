class PayLinkAPI:
    """
    API simulada de PayLink.
    El método makePayment no retorna nada (void) y lanza excepciones si hay parámetros inválidos.
    """

    def __init__(self, merchant_id: str = "DEMO-MERCHANT") -> None:
        self.merchant_id = merchant_id

    def makePayment(self, total: float, isoCurrency: str) -> None:
        """
        Procesa un pago.

        Args:
            total (float): Monto a pagar. Debe ser > 0.
            isoCurrency (str): Código ISO 4217 de 3 letras (p. ej., 'USD', 'CRC').

        Raises:
            TypeError: Si total no es numérico.
            ValueError: Si total <= 0 o isoCurrency no es un código ISO válido.
        """
        # Validaciones
        if not isinstance(total, (int, float)):
            raise TypeError("total debe ser numérico")
        if total <= 0:
            raise ValueError("total debe ser mayor a 0")
        if not isinstance(isoCurrency, str) or len(isoCurrency) != 3 or not isoCurrency.isalpha():
            raise ValueError("isoCurrency debe ser un código ISO 4217 de 3 letras")

        iso = isoCurrency.upper()

        # Simulación de llamada a la pasarela de pagos
        # En una integración real, aquí iría la llamada HTTP/SDK a PayLink
        print(f"[PayLinkAPI] Merchant={self.merchant_id} procesando pago de {total:.2f} {iso}...")
        print("[PayLinkAPI] Pago aprobado.")