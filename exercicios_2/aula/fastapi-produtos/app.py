from fastapi import FastAPI
from models.products import Product, CreateProduct

app = FastAPI()

data = [
    Product(id=1, name="Produto 1", description="Descrição do Produto 1", price=10.0),
    Product(id=2, name="Produto 2", description="Descrição do Produto 2", price=20.0),
    Product(id=3, name="Produto 3", description="Descrição do Produto 3", price=30.0),
]

@app.get("/api/products")
def get_produtos():
    return data

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for product in data:
        if product.id == product_id:
            return product
    return {"message": "Nenhum produto não encontrado com este ID"}

@app.post("/api/products")
def create_product(product: CreateProduct):
    new_product = Product(id=len(data)+1, **product.dict())
    data.append(new_product)
    return new_product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(data):
        if product.id == product_id:
            deleted = data.pop(i)
            return {
                'message': 'Produto deletado com sucesso!',
                'deleted': deleted
            }
    return {'message': 'ID não encontrado...'}

@app.put("/api/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(data):
        if product.id == product_id:
            data[i] = updated_product
            return {
                'message': 'Produto atualizado com sucesso!',
                'updated': updated_product
            }
    return {'message': 'ID não encontrado...'}