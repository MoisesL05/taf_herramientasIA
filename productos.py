import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)

TOTAL_PRODUCTOS = 75000

categorias = [
    "Electronica",
    "Ropa",
    "Hogar",
    "Deportes",
    "Belleza",
    "Juguetes",
    "Automotriz",
    "Oficina",
    "Salud",
    "Tecnologia"
]

productos_unicos = set()
datos = []

while len(productos_unicos) < TOTAL_PRODUCTOS:
    producto = (
        fake.word().capitalize() + " " +
        fake.word().capitalize() + " "
    )

    if producto not in productos_unicos:
        productos_unicos.add(producto)
        categoria = random.choice(categorias)
        datos.append([
            producto,
            categoria,
        ])

df = pd.DataFrame(
    datos,
    columns=[
        "producto",
        "categoria",
    ]
)

df.to_csv(
    "data/productos.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())

print("\nCantidad de productos creados:")
print(df.shape)