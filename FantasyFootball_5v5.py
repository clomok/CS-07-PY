print("""
555555555555555555                     555555555555555555 
5::::::::::::::::5                     5::::::::::::::::5 
5::::::::::::::::5                     5::::::::::::::::5 
5:::::555555555555                     5:::::555555555555 
5:::::5       vvvvvvv           vvvvvvv5:::::5            
5:::::5        v:::::v         v:::::v 5:::::5            
5:::::5555555555v:::::v       v:::::v  5:::::5555555555   
5:::::::::::::::5v:::::v     v:::::v   5:::::::::::::::5  
555555555555:::::5v:::::v   v:::::v    555555555555:::::5 
            5:::::5v:::::v v:::::v                 5:::::5
            5:::::5 v:::::v:::::v                  5:::::5
5555555     5:::::5  v:::::::::v       5555555     5:::::5
5::::::55555::::::5   v:::::::v        5::::::55555::::::5
 55:::::::::::::55     v:::::v          55:::::::::::::55 
   55:::::::::55        v:::v             55:::::::::55   
     555555555           vvv                555555555   
     _                         _                       
   _|_ _. ._ _|_  _.  _      _|_ _   _ _|_ |_   _. | | 
    | (_| | | |_ (_| _> \/    | (_) (_) |_ |_) (_| | | 
                       /                              
                      -PY-03-L5

Welcome to 5v5 Fantasy Football!!
Starting Salary Cap is set at $40 by default.
Please select 1 QB, 1 RB, 1 WR, 1 TE, and 1 DEF/S
Max Roster Amount = 5
Press "1" at any time to show list of available QBs
Press "2" at any time to show list of available RBs
Press "3" at any time to show list of available WRs
Press "4" at any time to show list of available TEs
Press "5" at any time to show list of available DEF/ST\n
""")
salary_cap = 40
roster = []

qb_list = {"Rodgers": 10, "Carr": 5, "Garoppolo": 1}
rb_list = {"Taylor": 10, "Chubb": 6, "Cook": 3}
wr_list = {"Kupp": 10, "Chase": 6, "Lockett": 2}
te_list = {"Kelce": 8, "Kittle": 5, "Pitts": 3}
def_list = {"Bills": 10, "Cowboys": 5, "Packers": 3}

print("\nAvailable Quarterbacks:\n")
for qb, qb_price in qb_list.items():
    print(qb, ": $", qb_price)
print("\nAvailable Running Backs:\n")
for rb, rb_price in rb_list.items():
    print(rb, ": $", rb_price)
print("\nAvailable Wide Receivers:\n")
for wr, wr_price in wr_list.items():
    print(wr, ": $", wr_price)
print("\nAvailable Tight Ends:\n")
for te, te_price in te_list.items():
    print(te, ": $", te_price)
print("\nAvailable Defense/Special Teams:\n")
for defst, def_price in def_list.items():
    print(defst, ": $", def_price)

print("Your starting salary cap is $40\n\n")

while True:
    if salary_cap <= 0:
        print("Good luck!\nHere are your players:\n")
        print(*roster, sep="\n")
        break
    else:
        player_choice = input(f"Select a player:\nPress \'1\' for QBs, \'2\' for RBs, \'3\' for WRs, \'4\' for TEs and \'5\' for DEF/ST\n\n>>").title()
        if player_choice == "1":
            print("Available Quarterbacks:\n")
            for qb, qb_price in qb_list.items():
                print(qb, ": $", qb_price, "\n")
        elif player_choice == "2":
            print("Available Running Backs: \n")
            for rb, rb_price in rb_list.items():
                print(rb, ": $", rb_price)
        elif player_choice == "3":
            print("Available Wide Receivers:\n")
            for wr, wr_price in wr_list.items():
                print(wr, ": $", wr_price)
        elif player_choice == "4":
            print("Available Tight Ends:\n")
            for te, te_price in te_list.items():
                print(te, ": $", te_price)
        elif player_choice == "5":
            print("Available Defense/Special Teams:\n")
            for defst, def_price in def_list.items():
                print(defst, ": $", def_price)
        elif player_choice in qb_list:
            if salary_cap >= qb_list[player_choice]:
                roster.append(player_choice)
                salary_cap -= qb_list[player_choice]
                if len(roster) == 5:
                    print("\n\nCongratulations, your roster is full. Here are your players:\n")
                    print(*roster, sep="\n")
                    break
                print(f"Your current roster: {roster} \nSalary Cap room: ${salary_cap}\n")
        elif player_choice in rb_list:
            if salary_cap >= rb_list[player_choice]:
                roster.append(player_choice)
                salary_cap -= rb_list[player_choice]
                if len(roster) == 5:
                    print("\n\nCongratulations, your roster is full. Here are your players:\n")
                    print(*roster, sep="\n")
                    break
                print(f"Your current roster: {roster} \nSalary Cap room: ${salary_cap}\n")
        elif player_choice in wr_list:
            if salary_cap >= wr_list[player_choice]:
                roster.append(player_choice)
                salary_cap -= wr_list[player_choice]
                if len(roster) == 5:
                    print("\n\nCongratulations, your roster is full. Here are your players:\n")
                    print(*roster, sep="\n")
                    break
                print(f"Your current roster: {roster} \nSalary Cap room: ${salary_cap}\n")
        elif player_choice in te_list:
            if salary_cap >= te_list[player_choice]:
                roster.append(player_choice)
                salary_cap -= te_list[player_choice]
                if len(roster) == 5:
                    print("\n\nCongratulations, your roster is full. Here are your players:\n")
                    print(*roster, sep="\n")
                    break
                print(f"Your current roster: {roster} \nSalary Cap room: ${salary_cap}\n")
        elif player_choice in def_list:
            if salary_cap >= def_list[player_choice]:
                roster.append(player_choice)
                salary_cap -= def_list[player_choice]
                if len(roster) == 5:
                    print("\n\nCongratulations, your roster is full. Here are your players:\n")
                    print(*roster, sep="\n")
                    break
                print(f"Your current roster: {roster} \nSalary Cap room: ${salary_cap}\n")
            else:
                print(f"You don't have enough money to add this player. Your current salary cap is {salary_cap}")
        else:
            print("Player not available. Press \"1-5\" to show available players.")

print("Have fun!")
