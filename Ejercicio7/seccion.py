from typing import Dict
from Music import MusicComponent



class Seccion(MusicComponent):
    """
    Flyweight: Representa secciones compartidas entre canciones
    Estado intrínseco: nombre, audio, duracion
    """
    
    def __init__(self, nombre: str, audio: str, duracion: int):
        self._nombre = nombre
        self._audio = audio  
        self._duracion = duracion
        print(f"   Sección '{nombre}' ({duracion}s)")
    
    def reproducir(self) -> None:
        print(f"      Reproduciendo sección: {self._nombre} ({self._duracion}s)")
    
    def get_duracion(self) -> int:
        return self._duracion
    
    def get_nombre(self) -> str:
        return self._nombre



class SeccionFactory:
    """
    Factory que gestiona el pool de secciones reutilizables
    Evita que la memoria se llene con datos que se repiten
    """
    
    def __init__(self):
        self._secciones: Dict[str, Seccion] = {}
    
    def get_seccion(self, nombre: str, audio: str, duracion: int) -> Seccion:
        """
        Obtiene una sección existente o crea una nueva
        """
        clave = nombre
        
        if clave not in self._secciones:
            self._secciones[clave] = Seccion(nombre, audio, duracion)
        else:
            print(f"Sección '{nombre}' ya existe")
        
        return self._secciones[clave]
    
    def get_estadisticas(self) -> str:
        """Retorna información sobre el pool de secciones"""
        total = len(self._secciones)
        secciones = ", ".join(self._secciones.keys())
        return f"Total de secciones únicas: {total} [{secciones}]"
