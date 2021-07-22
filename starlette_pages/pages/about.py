from starlette.responses import HTMLResponse


def response(request):
    return HTMLResponse("<h1>Test</h1>")