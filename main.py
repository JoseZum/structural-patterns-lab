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
    print("Ejercicio 7: Sistema de música con Flyweight")
  

    # Instanciar Factory (pool/flyweights)
    factory = SeccionFactory()

    print("\nCreando secciones ")
    intro_pop     = factory.get_seccion("Intro Pop",       "audio/intro_pop.mp3", 15)
    verso_std     = factory.get_seccion("Verso Estándar",  "audio/verso1.mp3",    30)
    coro_energico = factory.get_seccion("Coro Enérgico",   "audio/coro1.mp3",     45)
    puente_melo   = factory.get_seccion("Puente Melódico", "audio/puente.mp3",    20)

    print("\nCreando canciones")

    # Canción 1: Original
    cancion1 = Cancion("Summer Vibes", "The Waves", "Original")
    cancion1.agregar_seccion(intro_pop)
    cancion1.agregar_seccion(verso_std)
    cancion1.agregar_seccion(coro_energico)
    cancion1.agregar_seccion(verso_std)     
    cancion1.agregar_seccion(coro_energico)  
    cancion1.agregar_seccion(puente_melo)
    cancion1.agregar_seccion(coro_energico)

    # Canción 2: reutiliza el flyweight
    cancion2 = Cancion("Summer Vibes", "The Waves", "Acústica")
    cancion2.agregar_seccion(factory.get_seccion("Intro Pop",      "audio/intro_pop.mp3", 15))
    cancion2.agregar_seccion(factory.get_seccion("Verso Estándar", "audio/verso1.mp3",    30))
    cancion2.agregar_seccion(factory.get_seccion("Coro Enérgico",  "audio/coro1.mp3",     45))

    # Canción 3> nueva cancion
    cancion3 = Cancion("Ocean Dreams", "The Waves", "Original")
    cancion3.agregar_seccion(factory.get_seccion("Intro Pop",       "audio/intro_pop.mp3", 15))
    cancion3.agregar_seccion(factory.get_seccion("Verso Estándar",  "audio/verso1.mp3",    30))
    cancion3.agregar_seccion(factory.get_seccion("Puente Melódico", "audio/puente.mp3",    20))

    print("\nCreando playlists")
    playlist1 = Playlist("Favoritas")
    playlist1.agregar_cancion(cancion1)
    playlist1.agregar_cancion(cancion3)

    playlist2 = Playlist("Ejercicio")
    playlist2.agregar_cancion(cancion1)
    playlist2.agregar_cancion(cancion2)

    # Listar y reproducir
    playlist1.listar()
    playlist2.listar()
    playlist1.reproducir()

    # Demostración rápida de reutilización por nombre (misma clave -> mismo flyweight)
    print("\nReutilización por nombre")
    a = factory.get_seccion("Coro Enérgico", "audio/coro1.mp3", 45)   
    b = factory.get_seccion("Coro Enérgico", "audio/otro.mp3",  60)   
    print("   ¿a es b?", a is b)

    # Estadísticas unicamente demostrar patron
    print(f"\n{'='*60}")
    print("Estadisticas")
    print("   " + factory.get_estadisticas())
