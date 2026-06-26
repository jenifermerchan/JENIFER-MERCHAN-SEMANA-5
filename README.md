# Sistema de Gestión de Restaurante

**Estudiante:**
Jenifer Estefania Merchan Jauregui

## Descripción del Sistema
Un sistema modular en Python para gestionar platos y clientes en un restaurante, aplicando principios de la POO.

## Estructura del Proyecto

```text
repositorio_github/
│
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── cliente.py
│   │
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   │
│   └── main.py
│
└── README.md
```

## Tipos de Datos Utilizados
- `str`: Nombres de productos, clientes y del establecimiento.
- `int`: Números identificadores de mesa.
- `float`: Precios de los platos y bebidas.
- `bool`: Disponibilidad de pedidos y estado VIP del cliente.
- `list`: Tipo compuesto para almacenar las colecciones de objetos.