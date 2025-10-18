from datetime import datetime

class AuditService:
    """Servicio de auditoría para registrar las acciones del usuario."""

    @staticmethod
    def log_action(user, action, status, extra_info=""):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[AuditService] {ts} | {status} | Usuario={user.getUsername()} | Acción={action} {extra_info}")
