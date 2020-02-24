import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route


async def root(request: Request):
    data = await request.json()
    return JSONResponse({"response": data})


app = Starlette(routes=[Route("/", root, methods=["POST"])])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
