from support import Order

order1 = Order(order_id=1)
print(f"Order ID: {order1.order_id}, Status: {order1.status.value}")
order1.startProcessing()
print(f"Order ID: {order1.order_id}, Status: {order1.status.value}")
order1.ship()
print(f"Order ID: {order1.order_id}, Status: {order1.status.value}")
order1.deliver()
print(f"Order ID: {order1.order_id}, Status: {order1.status.value}")

order2 = Order(order_id=2)
print(f"Order ID: {order2.order_id}, Status: {order2.status.value}")
order2.startProcessing()
print(f"Order ID: {order2.order_id}, Status: {order2.status.value}")
order2.cancel()
print(f"Order ID: {order2.order_id}, Status: {order2.status.value}")

order3 = Order(order_id=3)
print(f"Order ID: {order3.order_id}, Status: {order3.status.value}")
try:
    order3.deliver()
except ValueError as e:
    print(f"Error: {e}")
    print(f"Order ID: {order3.order_id}, Status: {order3.status.value}")