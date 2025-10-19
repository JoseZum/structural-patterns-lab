from PaymentProvider import PaymentProvider

class PaymentProcessor:
    """
    Procesador de pagos concreto.
    processPayment(provider, amount, currency) no retorna valor (void).
    """

    def processPayment(self, provider: PaymentProvider, amount: float, currency: str) -> None:
        """
        Orquesta un pago usando el proveedor dado.
        """
        #validaciones
        if provider is None:
            raise ValueError("provider no puede ser None")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount debe ser numérico")
        if amount <= 0:
            raise ValueError("amount debe ser mayor a 0")
        if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
            raise ValueError("currency debe ser un código ISO 4217 de 3 letras")
        # Normalización para el currency upper case significa mayusculas
        iso = currency.upper()
        try:
            ok = provider.charge(amount, iso) #genera el cargo
            if ok:
                print(f"[PaymentProcessor] Pago exitoso: {amount:.2f} {iso}")
            else:
                print(f"[PaymentProcessor] Pago fallido: {amount:.2f} {iso}")
        except Exception as e:
            print(f"[PaymentProcessor] Error al procesar el pago: {e}")
