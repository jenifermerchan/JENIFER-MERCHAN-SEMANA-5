from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def ejecutar_sistema() -> None:
    # Instancia del restaurante
    mi_restaurante = Restaurante("Triple")

    print("--- INICIANDO CARGA DE DATOS ---")

    # Nuevos productos y precios modificados
    producto_uno = Producto("Arroz con Menestra y Carne", 5.25, True)
    producto_dos = Producto("Jugo de Guayaba", 1.00, False)

    mi_restaurante.agregar_producto(producto_uno)
    mi_restaurante.agregar_producto(producto_dos)

    # Nuevos nombres de clientes asignados
    cliente_uno = Cliente("Luis Mendoza", 5, True)
    cliente_dos = Cliente("Elena Anchundia", 3, False)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # Reporte final en consola
    mi_restaurante.mostrar_menu_y_clientes()


if __name__ == "__main__":
    ejecutar_sistema()