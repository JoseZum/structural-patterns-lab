from abc import ABC, abstractmethod

class MusicComponent(ABC):
    """Interfaz base para componentes musicales"""
    
    @abstractmethod
    def reproducir(self) -> None:
        pass
    
    @abstractmethod
    def get_duracion(self) -> int:
        pass
