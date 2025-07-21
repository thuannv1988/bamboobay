from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simulated database
stores = {
    "store1": {"name": "Store 1", "products": [{"id": 1, "name": "Shirt"}, {"id": 2, "name": "Shoes"}]},
    "store2": {"name": "Store 2", "products": [{"id": 3, "name": "Hat"}]}
}

products = {
    1: {"id": 1, "name": "Shirt", "desc": "Nice cotton shirt"},
    2: {"id": 2, "name": "Shoes", "desc": "Running shoes"},
    3: {"id": 3, "name": "Hat", "desc": "Cool summer hat"}
}

@app.route('/')
def home():
    return render_template("home.html", stores=stores)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = products.get(product_id)
    return render_template("product.html", product=product)

@app.route('/', subdomain="<store>")
def store_view(store):
    store_data = stores.get(store)
    if store_data:
        return render_template("store.html", store=store_data)
    return "Store not found", 404

if __name__ == '__main__':
    app.config['SERVER_NAME'] = "localhost:5000"  # for subdomain support
    app.run(debug=True)
