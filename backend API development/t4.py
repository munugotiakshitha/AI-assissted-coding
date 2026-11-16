from flask import Flask, request, jsonify

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Veg Burger", "price": 120},
    {"id": 2, "name": "Pasta", "price": 180},
]
orders = []


def next_order_id():
    return max((order["id"] for order in orders), default=0) + 1


@app.get("/menu")
def get_menu():
    """Return the available dishes."""
    return jsonify(menu), 200


@app.post("/order")
def place_order():
    """Place an order using a JSON list of items."""
    data = request.get_json(silent=True) or {}
    items = data.get("items")

    if not isinstance(items, list) or not items:
        return jsonify({"error": "Provide a non-empty items list"}), 400

    order = {
        "id": next_order_id(),
        "items": items,
        "status": "Placed",
    }
    orders.append(order)
    return jsonify(order), 201


@app.get("/order/<int:order_id>")
def get_order(order_id):
    """Return the details and status of an order."""
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order), 200


@app.put("/order/<int:order_id>")
def update_order(order_id):
    """Replace the items in an existing order."""
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json(silent=True) or {}
    items = data.get("items")

    if not isinstance(items, list) or not items:
        return jsonify({"error": "Provide a non-empty items list"}), 400

    order["items"] = items
    return jsonify(order), 200


@app.delete("/order/<int:order_id>")
def cancel_order(order_id):
    """Cancel an order by deleting it."""
    order = next((item for item in orders if item["id"] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    orders.remove(order)
    return jsonify({"message": "Order cancelled"}), 200


if __name__ == "__main__":
    app.run(debug=True)