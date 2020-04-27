#https://leetcode.com/problems/apply-discount-every-n-orders/
class Cashier:
    def __init__(self, n:int, discount:int, products:[], prices:[]):
        self.n = n
        self.data = {}
        for item, price in zip(products, prices):
            self.data[item] = price
        self.discount = discount
        self.count = 0

    def getBill(self, products, amount):
        price = 0
        self.count += 1
        for product,amt in zip(products, amount):
            price += self.data[product]*amt
        if self.count == self.n:
            price *= (1-self.discount/100)
            self.count = 0
        return price

a = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100])
print(a.getBill([1,2],[1,2]))
print(a.getBill([3,7],[10,10]))
print(a.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]))
print(a.getBill([4],[10]))
print(a.getBill([7,3],[10,10]))
print(a.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]))
print(a.getBill([2,3,5],[5,3,2]))


