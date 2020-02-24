from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def post(request: Request):
    return JSONResponse({"hello": "world"})


async def get(request: Request):
    return JSONResponse({"hello": "world"})


routes = [
    Route("/api/v1/order", post, methods=["POST"]),
    Route("/api/v1/order/{order_id:int}", get, methods=["GET"]),
]
