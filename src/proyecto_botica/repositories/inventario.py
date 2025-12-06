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

class RepositorioMemoria(IRepositorio):
    """
    Implementacion del repositorio en memoria.
    Almacena productos en un diccionario (key=id_producto).
    """

    def __init__(self):
        """Inicializa el almacenamiento en memoria."""
        self._productos: Dict[int, Producto] = {}

    def agregar(self, producto: Producto) -> bool:
        """Agrega un producto al repositorio."""
        if producto.id_producto in self._productos:
            raise ValueError(f"El producto con ID {producto.id_producto} ya existe")
        self._productos[producto.id_producto] = producto
        return True
    
    
    def obtener(self, id_producto: int) -> Optional[Producto]:
        """Obtiene un producto por ID."""
        return self._productos.get(id_producto)

    def obtener_todos(self) -> List[Producto]:
        """Obtiene todos los productos."""
        return list(self._productos.values())

    def eliminar(self, id_producto: int) -> bool:
        """Elimina un producto del repositorio."""
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False