import random


response=input("press y to roll the dice again and n to exit")
print("/n")

while response=="y":
    no=random.randint(1,6)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if no==2:
        print("[0---0]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[-----]")

    if no==3:
        print("[0---0]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")    

    if no==4:
        print("[0---0]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[0----]")  
        
    if no==5:
        print("[0---0]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[0---0]")   

    if no==6:
        print("[0---0]")
        print("[     ]")
        print("[0---0]")
        print("[     ]")
        print("[0---0]")     

          
