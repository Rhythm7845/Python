class Store:
    def __init__(self, c, p, n):
        self.name = n
        self.price = p
        self.code = c

        
    def SetQuantity(self):
        self.quant = int(input("Enter the quantity"))
    
    def GetInfo(self):
        print(self.name, "     ", self.price)
        
        
tea = Store(103, 20, "Tea")
coffee = Store(104, 50, "Cofee")

print("MENU:")
tea.GetInfo()
coffee.GetInfo()

tea.SetQuantity(int(input("Set Quantity: ")))
coffee.SetQuantity(int(input("Set Quantity: ")))
tea_p = tea.price * tea.quant
coffee_p = coffee.price * coffee.quant

total = tea_p + coffee_p
