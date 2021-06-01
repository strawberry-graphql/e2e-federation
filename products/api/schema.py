from typing import List

import strawberry
from strawberry import ID

from .types import Product


@strawberry.type
class Query:
    @strawberry.field
    def products_service(self) -> str:
        return "products"

    @strawberry.field
    def products(self) -> List[Product]:
        return [
            Product(id=ID("1"), name="Mango Ice Cream"),
            Product(id=ID("2"), name="Strawberry Ice Cream"),
        ]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, name: str) -> Product:
        return Product(id=ID("500"), name=name)


schema = strawberry.federation.Schema(query=Query, mutation=Mutation)
