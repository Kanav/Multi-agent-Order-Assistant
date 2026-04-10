"""
data/orders.py — Extended order database and delivery/refund policies.
"""

ORDER_DATABASE: dict = {
    "ORD-301": {
        "item_id": "DISH101",
        "item_name": "Pepperoni Pizza",
        "customer_name": "Rohan Patel",
        "customer_email": "rohan@example.com",
        "status": "Delivered",
        "price": 329,
        "order_date": "2026-04-01",
        "estimated_delivery": "2026-04-01 19:00",
        "tracking_id": "SS301TRK",
    },
    "ORD-302": {
        "item_id": "DISH102",
        "item_name": "Chicken Alfredo Pasta",
        "customer_name": "Ananya Singh",
        "customer_email": "ananya@example.com",
        "status": "Preparing",
        "price": 369,
        "order_date": "2026-04-02",
        "estimated_delivery": "2026-04-02 20:15",
        "tracking_id": "SS302TRK",
    },
    "ORD-303": {
        "item_id": "DISH104",
        "item_name": "Falafel Wrap",
        "customer_name": "Vikram Rao",
        "customer_email": "vikram@example.com",
        "status": "Out for Delivery",
        "price": 249,
        "order_date": "2026-04-03",
        "estimated_delivery": "2026-04-03 19:45",
        "tracking_id": "SS303TRK",
    },
    "ORD-304": {
        "item_id": "DISH107",
        "item_name": "Pad Thai",
        "customer_name": "Meera Iyer",
        "customer_email": "meera@example.com",
        "status": "Placed",
        "price": 339,
        "order_date": "2026-04-04",
        "estimated_delivery": "2026-04-04 20:30",
        "tracking_id": "SS304TRK",
    },
    "ORD-305": {
        "item_id": "DISH109",
        "item_name": "Chocolate Brownie",
        "customer_name": "Amit Verma",
        "customer_email": "amit@example.com",
        "status": "Delivered",
        "price": 149,
        "order_date": "2026-04-05",
        "estimated_delivery": "2026-04-05 18:45",
        "tracking_id": "SS305TRK",
    },
}


DELIVERY_POLICIES = """\
DELIVERY OPTIONS:
- Express (30 min): ₹49, available in metro cities
- Standard (60 min): ₹29
- Scheduled (choose time): Free on orders over ₹500

CANCELLATION & REFUND POLICY:
| Order Status       | Refund         | Processing Time   |
|--------------------|----------------|-------------------|
| Placed             | 100% refund    | 1-2 business days |
| Preparing          | 50% refund     | 2-3 business days |
| Out for Delivery   | No refund      | N/A               |
| Delivered          | No refund      | N/A               |

ESCALATION:
- Customers can request human support for unresolved complaints.
- Target response time: 30 minutes.
"""
