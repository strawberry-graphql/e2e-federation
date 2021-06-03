from typing import List, Optional

import strawberry
from strawberry import ID


@strawberry.type
class Order:
    id: ID
    customer_name: str


@strawberry.federation.type(keys=["id"], extend=True)
class Product:
    id: ID = strawberry.federation.field(external=True)
    name: str = strawberry.federation.field(external=True)

    @strawberry.federation.field(requires=["name"])
    def code(self) -> str:
        return f"OrderService:{self.name}"

    @strawberry.field
    def orders(self) -> List[Order]:
        if self.id == "1":
            return [Order(id=ID("1"), customer_name="Marco")]
        elif self.id == "2":
            return [Order(id=ID("2"), customer_name="Patrick")]
        elif self.id == "500":
            return [Order(id=ID("3"), customer_name="Ethan Winters")]
        else:
            return []

    @classmethod
    async def resolve_reference(cls, id: ID, name: Optional[str] = None):
        # type: ignore because of the mismatch of types because the argument
        # `name` here and the field `name` in Product
        # We need `Product#name` to be `str` as it needs the same type it has
        # in the other services, but since resolve_reference will send `name`
        # only when the field that requires it is queried, it might be null in some
        # cases
        return cls(id=id, name=name)  # type: ignore
