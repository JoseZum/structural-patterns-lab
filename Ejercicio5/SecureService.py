class SecureService:
    """Servicios críticos del sistema."""

    def generate_report(self, user):
        print(f"[SecureService] Generando reporte financiero para {user.getUsername()}... OK")

    def delete_record(self, user, record_id):
        print(f"[SecureService] Borrando registro sensible #{record_id}... OK")

    def deploy_service(self, user, target):
        print(f"[SecureService] Desplegando servicio en entorno '{target}'... OK")