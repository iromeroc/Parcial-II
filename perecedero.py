class Perecedero: 

    def __init__(self, nombre: str, precio: float, cantidad: int, fecha_caducidad: str ):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad