import aiohttp_jinja2
import jinja2
from aiohttp import web

from db import close_pg, init_pg
from middlewares import setup_middlewares
from routes import setup_routes, setup_static_routes
from settings import BASE_DIR, config

app = web.Application()


# loading configuration files
app["config"] = config

# setup middleware
setup_middlewares(app)

# setting up routes
setup_routes(app)

# setting up static
setup_static_routes(app)

# setting up database connection
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

# set-up templating engine
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / "aiohttpdemo_polls" / "templates")),
)

web.run_app(app)
