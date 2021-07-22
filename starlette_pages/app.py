from starlette.applications import Starlette
from .router import handle_routes


app = Starlette(
    debug=True,
    routes=handle_routes(),
)
