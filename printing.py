import reports
# Printing functions

def menu():
    switch_on = 1
    while switch_on == 1:

        mode = input("Please give me a number of the function:")

        if mode in "1234567":
            if mode == "1":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    print (reports.count_games(information1))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "2":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    print (reports.get_latest(information1))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "3":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    information2 = input("Please give me the genre:")
                    print (reports.count_by_genre(information1, information2))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "4":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    information2 = input("Please give me the title:")
                    print (reports.get_line_number_by_title(information1, information2))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "5":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    print (reports.sort_abc(information1))
                except:
                    print ("Invalid number, please try again")
                    continue

            if mode == "6":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    print (reports.get_genres(information1))
                except:
                    print ("Invalid number, please try again")
                    continue
            
            if mode == "7":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    print (reports.when_was_top_sold_fps(information1))
                except:
                    print ("Invalid number, please try again")
                    continue
            
            
            exitQuestion = input("If would you like to ask another question please press 1 button and for exit push any other button: ")
            if exitQuestion != "1":
                switch_on += 1


menu()