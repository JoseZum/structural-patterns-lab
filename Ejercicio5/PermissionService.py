class PermissionService:
    """Servicio para gestionar permisos de los usuarios."""

    def __init__(self):
        self._permissions = {
            "generate_report": {"admin", "supervisor"},
            "delete_record": {"admin"},
            "deploy_service": {"admin", "devops"}
        }

    def has_permission(self, user, action):
        """Verifica si el usuario tiene permisos para ejecutar la acción."""
        return user.getRole() in self._permissions.get(action, set())