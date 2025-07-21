from flask import Flask, render_template

app = Flask(__name__)

store_data = {
    "store1": [
        {"id": 1, "name": "Product A", "price": "$10"},
        {"id": 2, "name": "Product B", "price": "$15"},
    ],
    "store2": [
        {"id": 3, "name": "Product C", "price": "$20"},
        {"id": 4, "name": "Product D", "price": "$25"},
    ],
}

@app.route('/')
def home():
    return render_template("home.html", stores=store_data.keys())

@app.route('/store/<store_name>')
def store_page(store_name):
    if store_name in store_data:
        products = store_data[store_name]
        return render_template("store.html", store_name=store_name, products=products)
    else:
        return "Store not found", 404

@app.route('/product/<int:product_id>')
def product_page(product_id):
    for products in store_data.values():
        for product in products:
            if product["id"] == product_id:
                return render_template("product.html", product=product)
    return "Product not found", 404

if __name__ == "__main__":
    app.run(debug=True)
