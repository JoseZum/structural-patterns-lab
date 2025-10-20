from typing import List
from cancion import Cancion

class Playlist:
    """Lista de reproducción que contiene canciones"""
    
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._canciones: List[Cancion] = []
    
    def agregar_cancion(self, cancion: Cancion) -> None:
        self._canciones.append(cancion)
        print(f"   Agregada: {cancion}")
    
    def reproducir(self) -> None:

        print(f"Reproduciendo Playlist: '{self._nombre}'")

        for cancion in self._canciones:
            cancion.reproducir()
    
    def listar(self) -> None:
        print(f"\n Playlist: '{self._nombre}' ({len(self._canciones)} canciones)")
        for i, cancion in enumerate(self._canciones, 1):
            print(f"   {i}. {cancion}")
