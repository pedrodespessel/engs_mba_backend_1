from pydantic import BaseModel

class Product(BaseModel):
    """
    Modelo de dados para um produto.
    Atributos
    - id: identificador único (int)
    - name: nome do produto (str)
    - description: descrição do produto (str)
    - price: preço do produto (float)
    """
    id: int
    name: str
    description: str
    price: float

class CreateProduct(BaseModel):
    name: str
    description: str
    price: float