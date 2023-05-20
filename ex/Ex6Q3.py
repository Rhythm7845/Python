class Store:
    def __init__(self, c, p, n):
        self.name = n
        self.price = p
        self.code = c

        
    def SetQuantity(self):
        self.quant = int(input("Enter the quantity"))
    
    def GetInfo(self):
        print(self.name, "     ", self.price)
        
        
tea = Store(101, 10, "Tea")
coffee = Store(102, 30, "Cofee")
lemonade = Store(103, 20, "Lemonade")

print("MENU:")
tea.GetInfo()
coffee.GetInfo()
lemonade.getinfo()

tea.SetQuantity(int(input("Set Quantity: ")))
coffee.SetQuantity(int(input("Set Quantity: ")))
lemonade.SetQuantity(int(input("Set Quantity: ")))
tea_p = tea.price * tea.quant
coffee_p = coffee.price * coffee.quant

total = tea_p + coffee_p
