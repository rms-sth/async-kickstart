import pathlib

from views import index, poll

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/detail/", poll)


def setup_static_routes(app):
    app.router.add_static("/static/", path=PROJECT_ROOT / "static", name="static")
