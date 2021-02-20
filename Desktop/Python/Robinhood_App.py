import robin_stocks as r
import matplotlib.pyplot as plt
from datetime import date



class Robinghood_App:

    def __init__(self):
        self.class_id = 1
    
    def login(self):
        while True:
            r_username = input('Please enter your email address: ')
            r_pass = input('Please enter your password: ')
            r_mfa = input('Please enter MFA code: ')
            try:
                r.login(r_username, r_pass,expiresIn=86400,mfa_code=r_mfa)
                print("Loggin successful")
                break
            except:
                print("Unable to login using previously entered credentials")
                
    def logout(self):
        print('Logging you out.')
        r.logout()

    def simplifyList(self, in_list):
        for items in in_list:
            for k, v in items.items():
                print(k + ": " + v)


    def getPortfolio(self):
        self.portfolio = r.get_open_stock_positions()
        self.simplifyList(self.portfolio)


    def getGainLoss(self):
        self.getPortfolio()
        '''
        current_close = int(float(portfolio["market_value"]))
        previous_close = int(float(portfolio["portfolio_equity_previous_close"]))

        if(current_close > previous_close):
            gain = current_close - previous_close
            return "Gain", gain
        else:
            loss = previous_close - current_close
            #gain_loss_list.append(['loss', loss])
            return "Loss", loss
            
        '''
        
    def storeGainLoss(self, tup):
        today_date = date.today().strftime("%m/%d/%Y")
        if(tup[0] == "Gain"):
            gain_loss_timeline[today_date] = ["Gain", tup[1]]
        elif(tup[0] == "Loss"):
            gain_loss_timeline[today_date] = ["Loss", tup[1]]

def main():


    r_app = Robinghood_App()
    r_app.login()
    r_app.getGainLoss()
    r_app.logout()

    
main()
