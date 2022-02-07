money = int(input("How much money do you have?"))
shopping_cart = []
fruits = {"Apple": 5, "Raspberry": 10, "Lemon": 20}

while True:
    if money <= 0:
        print(f"Thanks for shopping! \nYou purchased {shopping_cart}")
        break
    else:
        print(f"you have ${money} left \nYou have {shopping_cart} in your cart")
        player_choice = input(f"Select a fruit {fruits}:").title()
        if player_choice in fruits:
            if money >= fruits[player_choice]:
                shopping_cart.append(player_choice)
                money -= fruits[player_choice]
            else:
                print("You don't have enough money to make this purchase.")
                print(f"Shopping cart: {shopping_cart}")
        else:
            print("Invalid choice.")