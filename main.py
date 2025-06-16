

from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse

app = FastAPI()

# Our product list - a dictionary where key is product id and value is product name
products = {1: "Sneakers", 2: "T-Shirt", 3: "Jeans", 4: "Sunglasses", 5: "Hat"}

# The shopping cart - a dictionary where key is product id and value is quantity
cart = {}


@app.get("/home", response_class=HTMLResponse)
async def get_home():
    return """
    <html>
        <head>
            <title> Welcome to Our Online Store </title>
        </head>
        <body>
            <p> Welcome to our online store! Check out our products <a href="/products">here</a>. </p>
        </body>
    </html>
    """

@app.get("/")
def read_root():
    return {"Welcome": "Welcome to our API!"}

@app.get("/say")
def sayHello():
    return{"Hallo":"Selamat Malam"}

@app.get("/products")
def get_products():
    return products

@app.post("/cart/{item_id}")
def add_to_cart(item_id: int):
    return {"message": f"Added item with id {item_id} to the cart"}

@app.delete("/cart/{item_id}")
def remove_from_cart(item_id: int):
    return {"message": f"Removed item with id {item_id} from the cart"}


@app.post("/cart/{product_id}")
def add_to_cart(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    return {"message": f"Added {products[product_id]} to the cart"}

@app.delete("/cart/{product_id}")
def remove_from_cart(product_id: int):
    if product_id not in cart:
        raise HTTPException(status_code=404, detail="Product not in cart")
    cart[product_id] -= 1
    if cart[product_id] == 0:
        del cart[product_id]
    return {"message": f"Removed {products[product_id]} from the cart"}

@app.get("/cart")
def get_cart():
    return {products[product_id]: quantity for product_id, quantity in cart.items()}



