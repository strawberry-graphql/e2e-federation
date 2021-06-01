import strawberry

from .types import Product


@strawberry.type
class Query:
    @strawberry.field
    def orders_service(self) -> str:
        return "orders"


schema = strawberry.federation.Schema(query=Query, types=[Product])
