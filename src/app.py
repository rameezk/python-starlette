import uvicorn
import os
from starlette.applications import Starlette
import databases

from api import get_routes
from api.handler.exception import exception_handlers

ENVIRONMENT = os.environ.get("ENVIRONMENT")
DATABASE_URL = os.environ.get("DATABASE_URL")


debug = False
reload = False
if ENVIRONMENT == "DEV":
    debug = True
    reload = True

database = databases.Database(DATABASE_URL)


app = Starlette(
    routes=get_routes(),
    on_startup=[database.connect],
    on_shutdown=[database.disconnect],
    debug=debug,
    exception_handlers=exception_handlers,
)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=reload)
