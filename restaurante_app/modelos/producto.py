class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre: str = nombre
        self.precio: float = precio
        self.disponible: bool = disponible

    def __str__(self) -> str:
        estado = "Disponible para pedir" if self.disponible else "Agotado por el momento"
        return f"{self.nombre} -> Precio: ${self.precio:.2f} [{estado}]"