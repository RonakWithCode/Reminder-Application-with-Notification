import time
from plyer import *
if __name__ == '__main__':
        while True:        
                notification.notify(title = "**Please Drink Water Now!!",
                message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
                # app_icon = "icon_of_python.ico",
                timeout= 9)
                time.sleep(2*1) # Add a time to
