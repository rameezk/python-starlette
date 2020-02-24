from json import JSONDecodeError

from starlette.responses import JSONResponse


async def request_error(request, exc):
    return JSONResponse({"detail": "Invalid request"}, status_code=400)


exception_handlers = {JSONDecodeError: request_error}
