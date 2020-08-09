from aiohttp import web
from routes import setup_routes
from settings import config
from db import close_pg, init_pg

app = web.Application()

# setting up routes
setup_routes(app)

# setting up database connection
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

# loading configuration files
app["config"] = config

web.run_app(app)

