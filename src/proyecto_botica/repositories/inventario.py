"""
Modulo de Repositorio - Inventario
Define las interfaces y servicios de acceso a datos
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from ..models.producto import Producto, Categoria

class IRepositorio(ABC):
    """Interfaz para el repositorio de productos (Abstracción)."""

    @abstractmethod
    def agregar(self, producto: Producto) -> bool:
        """Agrega un producto."""
        pass

    @abstractmethod
    def obtener(self, id_producto: int) -> Optional[Producto]:
        """Obtiene un producto por ID."""
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Producto]:
        """Obtiene todos los productos."""
        pass
    
    @abstractmethod
    def eliminar(self, id_producto: int) -> bool:
        """Elimina un producto."""
        pass
