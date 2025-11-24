money_list = []       
total_money = 0        

print("Hi! Welcome to my Money Tracker")
print("I made this to help me not spend too much")
print()

while True:
    
    print("What do you want to do?")
    print("1 - Add money I got (income)")
    print("2 - Add money I spent (expense)")
    print("3 - See all and how much I have")
    print("4 - Bye bye, finish")
    print()
    
    what = input("Choose number 1 2 3 or 4: ")
    
    if what == "1":
        print()
        print("--- Add Income ---")
        name = input("What is this money for? (like Salary): ")
        how_much = input("How much? $")
        
     
        how_much = float(how_much)
     
        money_list.append( ["income", name, how_much] )
        total_money = total_money + how_much
        
        print("Okay! I added $", how_much)
        print("Now you have $", total_money)
        print()
        
    elif what == "2":
        print()
        print("--- Add Expense ---")
        name = input("What did you buy? (like Food): ")
        how_much = input("How much did it cost? $")
        
        how_much = float(how_much)
        
        money_list.append( ["expense", name, how_much] )
        total_money = total_money - how_much
        
        print("Okay, I removed $", how_much)
        print("Now you have $", total_money)
        print()
        
    elif what == "3":
        print()
        print("*** All my money things ***")
        print()
        
        if len(money_list) == 0:
            print("Nothing here yet!")
        else:
            for thing in money_list:
                if thing[0] == "income":
                    print(" +", thing[2], "  -", thing[1])
                else:
                    print(" -", thing[2], "  -", thing[1])
        
        print()
        print("Total money now =", total_money)
        
        if total_money >= 0:
            print("Good! You have money left")
        else:
            print("Oh no! You spent more than you have")
            
        print()
        
    elif what == "4":
        print()
        print("Thank you for using my program!")
        print("See you next time")
        break
        
    else:
        print()
        print("Please type only 1, 2, 3 or 4")
        print()