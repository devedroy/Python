class Store:
    
    Discount = 0.0

    def __init__(self, ID, Type, Price, Discount):
        self.ID = ID
        self.Type = Type
        self.Price = Price
        self.Discount = Discount

#main
Toy = Store(1, "Toy", 100, 10)