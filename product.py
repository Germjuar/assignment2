class Product:

    def __init__(self, name: str, stock: int, price: float) -> None:
        self.name: str = name
        self.stock: int = stock
        self.price: float = price

    def __str__(self) -> str:
        # Implementation for displaying name, price, and stock
        return f'{self.name}: ${self.price:.2f}, ({self.stock} in stock)'
