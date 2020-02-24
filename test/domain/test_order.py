import unittest

from domain.order import Order
from domain.events.order import OrderCreated, StatusChanged


class OrderTest(unittest.TestCase):
    def test_should_create_order(self):
        order = Order.create(user_id=1)
        self.assertEqual(order.changes, [OrderCreated(user_id=1)])

    def test_should_return_correct_status(self):
        order = Order.create(user_id=2)
        order.set_status("paid")
        self.assertEqual(
            order.changes, [OrderCreated(user_id=2), StatusChanged("paid")]
        )
