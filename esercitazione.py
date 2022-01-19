# How to create a class:
#class Item:
 #   def calculate_total_price(self, x, y):
 #       return x * y

# How to create an instance of a class
#item1 = Item()

# Assign attributes:
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5

# Calling methods from instances of a class:
#print(item1.calculate_total_price(item1.price, item1.quantity))

# How to create an instance of a class (We could create as much as instances we'd like to)
#item2 = Item()

# Assign attributes
#item2.name = "Laptop"
#item2.price = 1000
#item2.quantity = 3

# Calling methods from instances of a class: 
#print(item2.calculate_total_price(item2.price, item2.quantity))

#class Item:
#    name = ""
#    price = ""
#    quantity = ""

#    def __init__(self, name, price, quantity):
#        self.name = name
#        self.price = price
#        self.quantity = quantity

#        if quantity < 0:
#            print("Errore: La quantità non può essere minore di zero.")
#        if price < 0:
#            print("Errore: Il prezzo non può essere minore di zero.")
#        else:
#            print(name, price, quantity)

#    def calcolo_prezzo_totale(self, price, quantity):
#        prezzo_totale = price * quantity
#        print("Il prezzo totale è: " + prezzo_totale)

#itemuno = Item
#itemuno.__init__()
#itemuno.calcolo_prezzo_totale()

class Item:
    def __init__(self, name: str, price: float, quantity= 0):
        assert price > 0, "Errore: Il prezzo non può essere inferiore di zero"
        assert quantity > 0, "Errore: la quantità non può essere minore di zero"

        self.name = name
        self.price = price
        self.quantity = quantity
    def calcola_prezzo_totale(self):
        return self.price * self.quantity

itemuno = Item("Telefono", 100, 5)
itemdue = Item("Computer", 200 , 3)
print(itemuno.calcola_prezzo_totale())
print(itemdue.calcola_prezzo_totale())