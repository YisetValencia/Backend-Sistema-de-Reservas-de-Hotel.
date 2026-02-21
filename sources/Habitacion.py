class Habitacion:
    def __init__(
        self, id: str, numero_habitacion: int, tipo_habitacion: str, precio: float
    ):
        self.id = id
        self.numero = numero_habitacion
        self.tipo = tipo_habitacion
        self.precio = precio
        self.__disponible = True

    def esta_disponible(self) -> bool:
        return self.__disponible

    def ocupar(self) -> None:
        if not self.__disponible:
            print(f"La habitación {self.numero} no está disponible.")
        self.__disponible = False

    def liberar(self) -> None:
        if self.__disponible:
            print(f"La habitación {self.numero} ya está disponible.")
        self.__disponible = True

    def calcular_costo(self, dias: int) -> float:
        if dias <= 0:
            print("El número de días debe ser mayor que cero.")
            return 0
        return dias * self.precio

    def __str__(self) -> str:
        disponibilidad = "Disponible" if self.__disponible else "Ocupada"
        return f"ID: {self.id} - Habitación {self.numero} - Tipo: {self.tipo} - Precio: ${self.precio:.2f} - {disponibilidad}"
