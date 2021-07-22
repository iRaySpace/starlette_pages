from starlette.responses import HTMLResponse


def response(request):
    return HTMLResponse("<h1>Dashboard</h1>")
