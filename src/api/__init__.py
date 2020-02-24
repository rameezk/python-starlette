from itertools import chain

from .order import routes as order_routes


def get_routes():
    return chain(order_routes)
