from json import JSONDecodeError

import uvicorn
import os
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from api import get_routes

environment = os.environ.get("ENVIRONMENT")

debug = False
reload = False
if environment == "DEV":
    debug = True
    reload = True


async def request_error(request, exc):
    return JSONResponse({"detail": "Invalid request"}, status_code=400)


exception_handlers = {JSONDecodeError: request_error}

app = Starlette(routes=get_routes(), debug=debug, exception_handlers=exception_handlers)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=reload)
