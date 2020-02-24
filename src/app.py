import uvicorn
import os
from starlette.applications import Starlette

from api import get_routes
from api.handler.exception import exception_handlers

environment = os.environ.get("ENVIRONMENT")

debug = False
reload = False
if environment == "DEV":
    debug = True
    reload = True


app = Starlette(routes=get_routes(), debug=debug, exception_handlers=exception_handlers)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=reload)
