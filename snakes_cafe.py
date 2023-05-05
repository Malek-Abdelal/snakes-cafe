Menu = { "Appetizers" : ["Wings",'Cookies', "Spring Rolls"],
        "Entrees" : ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
        "Desserts" : ["Ice Cream", "Cake", "Pie"],
        "Drinks" : ["Coffee", "Tea", "Unicorn Tears"] }


def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
************************************** \n
''')

    for key, value in Menu.items():
        print( f"{key}\n-------")
        for item in value:
            print(item)
        print("\n")
    
    print('''***********************************
** What would you like to order? **
***********************************
''')


def user_insertion():
    user_input=input(">")  
    return user_input.title()        


def main():
    user_input = user_insertion()
    customer_meal = {}

    while(user_input.lower() != "quit"):
        item_exist = False
        for items in Menu.values():
            if user_input in items:
                item_exist = True
                if user_input in customer_meal: 
                    customer_meal[user_input][0] += 1
                    customer_meal[user_input][1] = "s "
                else: 
                    customer_meal[user_input] = [1, " "]

                # print(customer_meal)
                print( f"** {customer_meal[user_input][0]} order{customer_meal[user_input][1]}of {user_input} has been added to your meal **")
                
        if item_exist == False:
            print("sorry we dont have this item !")
            
        user_input = user_insertion()   

    end_application()


def end_application():
    print("Thanks for using snakes cafe application !")          

if __name__=="__main__": 
    intro()  
    main()
                 