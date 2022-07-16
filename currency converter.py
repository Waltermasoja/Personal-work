import time
class currency_conv():
    def __init__(self) -> None:
       pass
    def ZAR_USD(self):
        self.amount = int(input("enter the amount you want to convert from Rands to Rands to USD:"))
        exchange_rate = 6.67
        converted = (self.amount /100) *exchange_rate
        print(converted) 
    def ZAR_POUND(self):
          self.amount = int(input("enter the amount you want to convert from Rands to POUNDS:"))
          rate = 8.67
          conver = (self.amount /100) *rate
          print(conver) 

class cons(currency_conv):
    print("Welcome to our awesome currency converter")
    time.sleep(3)
    con_cur = input("enter the currency you want to convert to : ")
    if con_cur == "USD":  
        cn=currency_conv()
        cn.ZAR_USD()
            
    elif con_cur == "POUND" :
        cn1=currency_conv()
        cn1.ZAR_POUND()  
    else:
        pass 

scon = cons()
scon
