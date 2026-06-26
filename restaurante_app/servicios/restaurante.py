from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, nuevo_producto: Producto) -> None:
        self.lista_productos.append(nuevo_producto)
        print(f"[NUEVO PRODUCTO] Se añadió '{nuevo_producto.nombre}' a la carta.")

    def registrar_cliente(self, nuevo_cliente: Cliente) -> None:
        self.lista_clientes.append(nuevo_cliente)
        print(f"[RECEPCIÓN] Se asignó mesa a {nuevo_cliente.nombre_completo}.")

    def mostrar_menu_y_clientes(self) -> None:
        print(f"\n================ MATRIZ: {self.nombre_establecimiento.upper()} ================")

        print("\n--- PLATOS Y BEBIDAS ---")
        for producto in self.lista_productos:
            print(f" * {producto}")

        print("\n--- CLIENTES ATENDIDOS ---")
        for cliente in self.lista_clientes:
            print(f" * {cliente}")
        print("=======================================================")