from microbit import *


while True:
    EI = Image("00900:"
               "09090:"
               "90009:"
               "90009:"
               "09990")
               
    display.scroll('Hello, You!', delay=200)
    
    if button_a.is_pressed():
        display.scroll("Ik been Yair.", delay=200)
        
    if button_b.is_pressed():
        display.show(EI, delay=300)
        
    sleep(3000)