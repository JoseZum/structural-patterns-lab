import sys
import os

# Agregar la carpeta facade_pattern a sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Ejercicio5'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Ejercicio11'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Ejercicio7'))

#EJERCICIO 5 IMPORTS ----------------------------------------------
from Client import Client
from Facade import Facade

#EJERCICIO 7 IMPORTS ----------------------------------------------
from seccion import SeccionFactory
from cancion import Cancion
from playlist import Playlist

#EJERCICIO 11 IMPORTS ----------------------------------------------
from PaymentProcessor import PaymentProcessor
from FastPayAdapter import FastPayAdapter
from PayLinkAdapter import PayLinkAdapter
from SafeTransferAdapter import SafeTransferAdapter
from FastPayService import FastPayService
from PayLinkAPI import PayLinkAPI
from SafeTransferClient import SafeTransferClient


if __name__ == "__main__":
    #EJERCICIO 5 -------------------------------------------------------
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

    # EJERCICIO 11 --------------------------------------------------------
    print("\n--- Ejercicio 11: Procesamiento de pagos con adaptadores ---")
    # Instanciar servicios reales y sus adaptadores
    paymentProcessor = PaymentProcessor()

    fastPay_adapter = FastPayAdapter(FastPayService())
    payLink_adapter = PayLinkAdapter(PayLinkAPI())
    safeTransfer_adapter = SafeTransferAdapter(SafeTransferClient("DEMO-TOKEN-1234"))

    # Casos exitosos
    print("\n[Prueba OK] FastPayAdapter con 25.00 USD")
    paymentProcessor.processPayment(fastPay_adapter, 25.00, "usd")

    print("\n[Prueba OK] PayLinkAdapter con 10 CRC")
    paymentProcessor.processPayment(payLink_adapter, 10, "CRC")

    print("\n[Prueba OK] SafeTransferAdapter con 70.50 EUR")
    paymentProcessor.processPayment(safeTransfer_adapter, 70.50, "eur")

    # Casos de error de validación en el procesador (se capturan para continuar la demo)
    print("\n[Prueba Error] amount <= 0")
    try:
        paymentProcessor.processPayment(payLink_adapter, 0, "USD")
    except Exception as e:
        print(f"[Main] Error esperado: {e}")

    print("\n[Prueba Error] currency inválida (no ISO 4217)")
    try:
        paymentProcessor.processPayment(fastPay_adapter, 15, "US")
    except Exception as e:
        print(f"[Main] Error esperado: {e}")

    # EJERCICIO 7 --------------------------------------------------------
    print("\n--- Ejercicio 7: Sistema de música con Flyweight ---")
    
    # Instanciar Factory 
    factory = SeccionFactory()

    # Crear secciones compartidas
    intro = factory.get_seccion("Intro", "audio/intro.mp3", 15)
    verso = factory.get_seccion("Verso", "audio/verso.mp3", 30)
    coro = factory.get_seccion("Coro", "audio/coro.mp3", 40)

    # Canción 1: usa las secciones múltiples veces
    cancion1 = Cancion("Summer Vibes", "The Waves", "Original")
    cancion1.agregar_seccion(intro)
    cancion1.agregar_seccion(verso)
    cancion1.agregar_seccion(coro)
    cancion1.agregar_seccion(verso)  
    cancion1.agregar_seccion(coro)   

    # Reutiliza las mismas secciones (flyweights)
    cancion2 = Cancion("Ocean Dreams", "The Waves", "Remix")
    cancion2.agregar_seccion(factory.get_seccion("Intro", "audio/intro.mp3", 15))  
    cancion2.agregar_seccion(factory.get_seccion("Coro", "audio/coro.mp3", 40))    

    # Crear playlist y reproducir
    playlist = Playlist("Mi Playlist")
    playlist.agregar_cancion(cancion1)
    playlist.agregar_cancion(cancion2)
    playlist.listar()
    playlist.reproducir()

    # Demostrar reutilización al mostrar que mismo nombre = mismo objeto
    print("\n[flyweight] Comprobando reutilización:")
    a = factory.get_seccion("Coro", "audio/coro.mp3", 40)
    b = factory.get_seccion("Coro", "audio/otro.mp3", 60)
    print(f"¿Los objetos 'Coro' son el mismo? {a is b}")
    
    # Estadísticas
    print(f"\n{factory.get_estadisticas()}")
