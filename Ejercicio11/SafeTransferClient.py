class SafeTransferClient:
    """
    Cliente simulado de SafeTransfer.
    - Requiere un token en el constructor.
    - makeSecurePay(money: str, currencyCode: str) -> int
      Retorna 1 si el pago fue aprobado.
    """

    def __init__(self, token: str) -> None:
        if not isinstance(token, str) or not token.strip():
            raise ValueError("token inválido")
        self.token = token.strip()

    #metodo para hacer un pago seguro del servicio de ejemplo en especifico
    def makeSecurePay(self, money: str, currencyCode: str) -> int:
        """
        Procesa un pago seguro.

        Args:
            money (str): Monto como string (p. ej., '10.50').
            currencyCode (str): Código ISO 4217 de 3 letras.

        Returns:
            int: 1 si aprobado; 0 si rechazado.

        Raises:
            TypeError/ValueError en caso de parámetros inválidos.
        """
        if not isinstance(money, str):
            raise TypeError("money debe ser str")
        if not isinstance(currencyCode, str) or len(currencyCode) != 3 or not currencyCode.isalpha():
            raise ValueError("currencyCode debe ser un código ISO 4217 de 3 letras")

        # Parseo del monto
        try:
            amount = float(money)
        except Exception:
            raise ValueError("money debe representar un número válido")

        if amount <= 0:
            raise ValueError("money debe ser mayor a 0")

        iso = currencyCode.upper()
        masked = f"...{self.token[-4:]}" if len(self.token) >= 4 else "***"
        print(f"[SafeTransferClient] Token={masked} procesando {amount:.2f} {iso} de forma segura...")
        print("[SafeTransferClient] Pago aprobado.")
        return 1