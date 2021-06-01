import strawberry
from strawberry import ID


@strawberry.federation.type(keys=["id"])
class Product:
    id: ID
    name: str
