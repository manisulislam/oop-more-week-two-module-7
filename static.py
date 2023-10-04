class Shop:
    cart =[] #static attribute or # class attribute
    origin= "china"

    def __init__(self, name , location) -> None:
        self.name= name
        self.location= location
    def purchase(self, item, price, amount):
        remaining= amount-price
        print(f"buying : {item} is price :{price} and remainig : {remaining}")
    @classmethod
    def dekhi(self, item):
        print(f"amne dekhi {item}")

    
    @staticmethod
    def multiply(a,b):
        result= a*b
        print(result)

dokan= Shop("book er dokan","sultanpur")
dokan.dekhi("physics")
Shop.purchase("a", "pen", 500, 2000)
Shop.dekhi("book")

Shop.multiply(5,8)
dokan.multiply(6,9)