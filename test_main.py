from assignment2.main import Product, Inventory

class TestInventory:
    def test_product_class(self):
        product = Product("Banana", 99, 100)
        assert product.stock == 99
        assert product.name == "Banana"
        assert product.price == 100

    def test_inventory_constructor(self):
        names = ["Apple", "Cucumber"]
        stocks = [55, 66]
        prices = [1.99, 2.99]
        inventory = Inventory(names, stocks, prices)

        products = inventory.get_products()
        assert len(products) == 2
        assert products[0].name == "Apple"
        assert products[0].stock == 55
        assert products[0].price == 1.99

        assert products[1].name == "Cucumber"
        assert products[1].stock == 66
        assert products[1].price == 2.99

    def assert_product(self, product, name, stock, price):
        assert name in product.__str__()
        assert stock in product.__str__()
        assert price in product.__str__()
