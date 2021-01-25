class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def get_total_price(self):
        # get the cost of each product in an array
        prices_of_stock = list(
            map(lambda x: x.price * x.available_stock, [self.products]))

        # sum of the total for the cost of all the products in the store
        total_price = reduce(lambda x, y: x + y, [prices_of_stock])

    def __str__(self):
        return f"This store has {len(self.products)} distinct products"
