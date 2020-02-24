from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from domain.order import Order


async def post(request: Request):
    data = await request.json()

    user_id = data.get("user_id", None)
    if user_id:
        order = Order.create(user_id)
        return JSONResponse(
            {"order": {"user_id": order.user_id, "status": order.status}},
            status_code=201,
        )
    return JSONResponse({"error": "no user_id sent"}, status_code=400)


async def get(request: Request):
    order_id = request.path_params["order_id"]
    return JSONResponse({"order_id": order_id})


routes = [
    Route("/api/v1/order", post, methods=["POST"]),
    Route("/api/v1/order/{order_id:int}", get, methods=["GET"]),
]
