class FastPayService:
    """
    Servicio externo que recibe un XML y devuelve un resultado como String.
    """

    def sendPaymentXML(self, xmlData: str) -> str:
        """
        Envía un pago en formato XML.

        Args:
            xmlData (str): XML con los datos del pago.

        Returns:
            str: Respuesta del servicio, p. ej. "<response>APPROVED</response>".

        Raises:
            TypeError: Si xmlData no es str.
            ValueError: Si xmlData está vacío o le faltan campos básicos.
        """
        # Validaciones básicas
        if not isinstance(xmlData, str):
            raise TypeError("xmlData debe ser str")
        xml = xmlData.strip()
        if not xml:
            raise ValueError("xmlData no puede estar vacío")
        if "<total>" not in xml or "<currency>" not in xml:
            raise ValueError("XML inválido: faltan campos obligatorios")

        print(f"[FastPayService] Enviando XML: {xml}")
        # Simulación de respuesta exitosa
        return "<response>APPROVED</response>"