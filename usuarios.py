import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)

TOTAL_USUARIOS = 260000

paises = [
    "Ecuador",
    "Colombia",
    "Peru",
    "Chile",
    "Argentina",
    "Mexico",
    "España",
    "Estados Unidos",
    "Brasil",
    "Uruguay",
    "Paraguay",
    "Bolivia",
    "Venezuela",
    "Panama",
    "Costa Rica"
]

usuarios_unicos = set()
datos = []

while len(usuarios_unicos) < TOTAL_USUARIOS:
    nombre_completo = fake.name()
    if nombre_completo not in usuarios_unicos:
        usuarios_unicos.add(nombre_completo)
        pais = random.choice(paises)
        edad = random.randint(18, 80)
        datos.append([
            nombre_completo,
            pais,
            edad
        ])

df = pd.DataFrame(
    datos,
    columns=[
        "usuario",
        "pais",
        "edad"
    ]
)

df.to_csv(
    "data/usuarios.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())

print("\nCantidad de usuarios:")
print(df.shape)