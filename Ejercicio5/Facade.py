from SecureService import SecureService
from AuditService import AuditService
from PermissionService import PermissionService


class Facade:
    """Facade que simplifica la interacción con múltiples servicios."""
    
    def __init__(self):
        self.secure_service = SecureService()
        self.audit_service = AuditService()
        self.permission_service = PermissionService()

    def generate_report(self, user):
        """Facade para generar el reporte."""
        if self.permission_service.has_permission(user, "generate_report"):
            self.audit_service.log_action(user, "generate_report", "ALLOW")
            self.secure_service.generate_report(user)
        else:
            self.audit_service.log_action(user, "generate_report", "DENY")
            print("[Facade] Acceso denegado: el usuario no tiene permisos para generar reportes.")

    def delete_record(self, user, record_id):
        """Facade para borrar el registro."""
        if self.permission_service.has_permission(user, "delete_record"):
            self.audit_service.log_action(user, "delete_record", "ALLOW", f"Registro #{record_id}")
            self.secure_service.delete_record(user, record_id)
        else:
            self.audit_service.log_action(user, "delete_record", "DENY", f"Registro #{record_id}")
            print(f"[Facade] Acceso denegado: el usuario no tiene permisos para borrar el registro #{record_id}.")

    def deploy_service(self, user, target):
        """Facade para desplegar el servicio."""
        if self.permission_service.has_permission(user, "deploy_service"):
            self.audit_service.log_action(user, "deploy_service", "ALLOW", f"En entorno '{target}'")
            self.secure_service.deploy_service(user, target)
        else:
            self.audit_service.log_action(user, "deploy_service", "DENY", f"En entorno '{target}'")
            print(f"[Facade] Acceso denegado: el usuario no tiene permisos para desplegar en '{target}'.")
