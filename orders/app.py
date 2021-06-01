from api.schema import schema
from starlette.applications import Starlette
from starlette.routing import Route

from strawberry.asgi import GraphQL


app = Starlette(debug=True, routes=[Route("/graphql", GraphQL(schema))])
