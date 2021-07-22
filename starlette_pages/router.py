from importlib import import_module
from starlette.responses import HTMLResponse
from starlette.routing import Route

def _route(request):
    page = request.path_params.get("page").lower()
    module = import_module(f"{__package__}.pages.{page}")
    return module.response(request)


def handle_routes():
    return [
        Route("/{page}", _route),
    ]
