from flask import Flask, render_template 

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": 29.99, "description": "Description of product 1"},
    {"id": 2, "name": "Product 2", "price": 49.99, "description": "Description of product 2"},
    {"id": 3, "name": "Product 3", "price": 19.99, "description": "Description of product 3"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
