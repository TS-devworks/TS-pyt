'''Trista Smith
12 October 2022
Low Battery Desktop Notification'''

import psutil
from win10toast import ToastNotifier

tn = ToastNotifier() #initialize 

def alert(title, msg, duration = 10):
    tn.show_toast(title, msg, duration=duration,
        icon_path= "C:/Users/TJ/Pyt/Python/desktop_notify/critical_icon.ico")

#Loop - if computer is plugged in: program stops - else if % is less than 30 alert notifies until plugged in
while True:
   percent = psutil.sensors_battery().percent #gets battery %
   if psutil.sensors_battery().power_plugged is True: #checks if computer is plugged in 
    continue
   elif percent < 30 and psutil.sensors_battery().power_plugged is False:
        msg = "Plug in charger NOW \nLike I'm about to shut off on you!"
        alert(f"CRITICALLY LOW: {percent}%", msg)
        print("Current Battery Life:", str(percent) + '%')
   










        

        
    
    
    





