from flask import Flask, jsonify

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "name": "Laptop",
        "quantity": 25,
        "price": 55000
    },
    {
        "id": 2,
        "name": "Mobile",
        "quantity": 40,
        "price": 20000
    },
    {
        "id": 3,
        "name": "Headphones",
        "quantity": 15,
        "price": 2500
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "E-Commerce Inventory Service is running"
    })

@app.route("/inventory")
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>")
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)