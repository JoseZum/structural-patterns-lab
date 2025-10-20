from typing import List
from Music import MusicComponent
from seccion import Seccion

#Aqui se almacena las secciones compartidas
class Cancion(MusicComponent):
    """
    Canción con titulo, artista, version
    """
    
    def __init__(self, titulo: str, artista: str, version: str = "Original"):
        self._titulo = titulo
        self._artista = artista
        self._version = version
        self._secciones: List[Seccion] = []
    
    def agregar_seccion(self, seccion: Seccion) -> None:
        """Agrega una sección a la canción"""
        self._secciones.append(seccion)
    
    def reproducir(self) -> None:
        print(f"\n'{self._titulo}' - {self._artista} [{self._version}]")
        for seccion in self._secciones:
            seccion.reproducir()
    
    def get_duracion(self) -> int:
        return sum(seccion.get_duracion() for seccion in self._secciones)
    
    def __str__(self) -> str:
        return f"{self._titulo} - {self._artista} [{self._version}] ({self.get_duracion()}s)"
