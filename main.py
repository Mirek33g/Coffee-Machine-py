from ingredients import menu, resources 
from replit import clear 
from logo import logo

# variables with resources 
water = resources["water"]
coffee = resources["coffee"] 
milk = resources["milk"] 



def check_sufficient(w, c, m = 0):
  if w <= water and c <= coffee and m <= milk:
    return True 


# gets information from user what coins they want to use and calculates the total 
def insert_coins():
  q = int(input("How many quarters? "))
  d = int(input("How many dimes? "))
  n = int(input("How many nickles? "))
  p = int(input("How many pennies? "))
  total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
  return total
  

def coffee_machine(type):
  global water 
  global coffee 
  global milk 
  costs = menu[type]["cost"]
  
  if type:
    user_coins = insert_coins()
    
    if user_coins >= costs:
      if check_sufficient(menu[type]["ingredients"]["water"], menu[type]["ingredients"]["coffee"]):
        change = round(user_coins - menu[type]["cost"], 2)
        water -= menu[type]["ingredients"]["water"]
        coffee -= menu[type]["ingredients"]["coffee"]
        milk -= menu[type]["ingredients"]["milk"]
        print(f"Here is your {type} with {change} change.") 
        another = input("Would you like another coffee? Type 'y' or 'n'") 
        clear()

        if another == "y":
          return True
        elif another == "n":
          print("See you next time")
          return False 

      else:
        print("Sorry there is not enough ingredients")
        return False 
        
    else:
      print(f"Sorry {type} cost is {costs} and you gave ${user_coins}")
      another = input("would you like to try again? Type 'y' or 'n'")
      clear()

      if another == "y":
        return True
      elif another == "n":
        return False


run = True
while run:
  print(logo) 
  resor = input("Would you like to see resources? Type 'y' or 'n' ")
  if resor == "y":
    print(f"Water = {water}\ncoffee = {coffee}\nmilk = {milk}")
  coffee_type = input("What would you like? (espresso, latte, cappuccino)") 
  print("Quarters = $0.25, dimes = $0.10, nickels = $0.05, dimes = $ 0.01")
  run = coffee_machine(coffee_type)
