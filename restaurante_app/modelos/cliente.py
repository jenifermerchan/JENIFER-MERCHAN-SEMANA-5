class Cliente:
    def __init__(self, nombre_completo: str, mesa_asignada: int, es_frecuente: bool):
        self.nombre_completo: str = nombre_completo
        self.mesa_asignada: int = mesa_asignada
        self.es_frecuente: bool = es_frecuente

    def __str__(self) -> str:
        tipo_cliente = "Cliente VIP" if self.es_frecuente else "Cliente Nuevo"
        return f"{self.nombre_completo} | Ubicado en Mesa: {self.mesa_asignada} | Tipo: {tipo_cliente}"