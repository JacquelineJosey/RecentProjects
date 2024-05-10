#-------------------- 323 Improvements by Jacqueline Josey: ---------------------
#Hello! Welcome to my 323.py combo menu! Hope you enjoy! ^-^
#Round Source Code: https://www.freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python/
#"$" Source Code: https://flexiple.com/python/python-append-to-string

#------------------ Start Info: ---------------------
subtotal = 0
total = 0
tax = 0
order=["","","",0]

#------------- Main Loop Section: ------------
keepOrdering=True
while keepOrdering:
    #------------- Sandwich Section: ------------
    sandwich = input("Would you like a sandwich? (y/n) ")
    while sandwich!="y" and sandwich!="n":
        sandwich = input("Would you like a sandwich? (y/n) ")
    if sandwich =="y":
        sandwich = input("Which sandwich would you like? chicken (c) $5.25, beef (b) $6.25, tofu (t) $5.25 " )
        while sandwich!="c" and sandwich!="b" and sandwich!="t":
            sandwich = input("Which sandwich would you like? chicken (c) $5.25, beef (b) $6.25, tofu (t) $5.25 " )
        if sandwich == "c":
                subtotal+=5.25
                sandwich="chicken sandwich"
        elif sandwich == "b":
                subtotal+=6.25
                sandwich="beef sandwich"
        elif sandwich == "t":
                subtotal+=5.25
                sandwich="tofu sandwich"
    elif sandwich =="n":
            subtotal+=0    
    order[0]=sandwich

    #----------------- Drink Section: ---------------------
    drink = input("Would you like a drink? (y/n) ")
    while drink!="y" and drink!="n":
        drink = input("Would you like a drink? (y/n) ")
    if drink =="y":
        drink = input("Which size? small (s) $1.00, medium (m) $1.75, large (l) $2.25 ")
        while drink!="s" and drink!="m" and drink!="l":
           drink = input("Which size? small (s) $1.00, medium (m) $1.75, large (l) $2.25 ")
        if drink == "s":
                subtotal+=1
        elif drink == "m":
                subtotal+=1.75
        elif drink == "l":
                child=input("Would you like a child size drink for only $.38 more? (y,n) ")
                while child!="y" and child!="n":
                    child=input("Would you like a child size drink for only $.38 more? (y,n) ")
                if child=="y":
                        drink="child"
                        subtotal+=2.25+.38
                elif child=="n":
                        subtotal+=2.25
                        drink="1"
    elif drink =="n":
            subtotal+=0
    order[1]=drink

    #-------------------- Fry Section: ----------------------
    fry = input("Would you like some fries? (y/n) ")
    while fry!="y" and fry!="n":
        fry = input("Would you like some fries? (y/n) ")
    if fry =="y":
        fry = input("Which size? small (s) $1.00, medium (m) $1.50, large (l) $2.00 ")        
        while fry!="s" and fry!="m" and fry!="l": 
            fry = input("Which size? small (s) $1.00, medium (m) $1.50, large (l) $2.00 ")  
        if fry == "s":
                subtotal+=1
        elif fry == "m":
                subtotal+=1.50
        elif fry == "l":
                mega=input("Would you like some mega size fries for only $.50 more? (y,n) ")
                while mega!="y" and mega!="n":
                   mega=input("Would you like some mega size fries for only $.50 more? (y,n) ")
                if mega=="y":
                        fry="mega"
                        subtotal+=2.00+.50
                elif mega=="n":
                        subtotal+=2.00
                        fry="1"
    elif fry =="n":
            subtotal+=0
    order[2]=fry

    #------------------- Ketchup Section: -------------------------
    ketchup = input("Would you like some ketchup? (y/n) ")
    while ketchup!="y" and ketchup!="n":
        ketchup =input("Would you like some ketchup? (y/n) ")
    if ketchup =="y":
            ketchup = int(input("How many? $.25 per packet "))
            subtotal+=(ketchup*.25)
    elif ketchup =="n":
            subtotal+=0
    order[3]=ketchup

    #--------------- Reciept Section: ------------------
    print(order)
    print(f'''
    Josey Fancy Diner
    sandwich:   {order[0]}
    drink:      {order[1]}
    fries:      {order[2]}
    ketchup:    {order[3]}

    ''')
    
    #---------------- Additonal Order Prompt: --------------
    orderAgain=input("Would you like to order again or checkout? (again/checkout) ")
    while orderAgain!="again" and orderAgain!="checkout":
       orderAgain=input("Would you like to order again or checkout? (again/checkout) ")
    if orderAgain=="checkout":
            keepOrdering=False
    elif orderAgain=="again":
            keepOrdering=True

#---------------- Rounded Total w/ Tax: ----------------
#7% tax
tax+=(subtotal*.07)
total+=(subtotal+tax)
money = "$"

rounded = round(total,2)

print(str(money) + str(rounded))

