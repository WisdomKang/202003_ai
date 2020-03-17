
class Card():
    charge_money:int

    def __init__(self):
        self.charge_money = 0
        
    def charge(self, money:int):
        self.charge_money += money
        print( "잔액이 {}원 입니다.".format(self.charge_money))

    def consume(self, money:int, store:str): 
        if store == "영화관": money = int( money * 0.8 )

        result = self.charge_money - money

        if result < 0 :
            print("잔액이 부족합니다.")
            return
        else : 
            print( "{}에서 {}원 사용했습니다.".format(store, money))
            self.charge_money -= money

    def __str__(self):
        return "잔액이 {}원 입니다.".format(self.charge_money)

    def print(self):
        print("잔액이 {}원 입니다.".format(self.charge_money))
