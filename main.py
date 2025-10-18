
from Ejercicio5.Client import Client
from Ejercicio5.Facade import Facade


if __name__ == "__main__":
    # Crear usuarios de ejemplo
    admin = Client("alice", "admin")
    employee = Client("bob", "employee")
    devops = Client("dora", "devops")
    supervisor = Client("sam", "supervisor")

    # Crear la fachada
    facade = Facade()

    print("\n--- Escenario 1: supervisor genera reporte ---")
    facade.generate_report(supervisor)

    print("\n--- Escenario 2: employee intenta borrar registro ---")
    facade.delete_record(employee, record_id="A-1023")

    print("\n--- Escenario 3: admin borra registro ---")
    facade.delete_record(admin, record_id="A-1023")

    print("\n--- Escenario 4: devops despliega servicio ---")
    facade.deploy_service(devops, target="staging")

    print("\n--- Escenario 5: employee intenta desplegar ---")
    facade.deploy_service(employee, target="prod")
