import reports
import os

def export(resolution):
    #open ("/home/gergo/Desktop/5 th week/1.txt", "w")
    if os.path.exists("/home/gergo/Desktop/5 th week/1.txt"):
        with open ("/home/gergo/Desktop/5 th week/1.txt", "a") as f:
            f.write(resolution)
            f.write("\n")    
    else:
        with open ("/home/gergo/Desktop/5 th week/1.txt", "w") as k:
            k.write (resolution)
            k.write("\n") 

# export(str(reports.count_games("/home/gergo/Desktop/5 th week/game_stat.txt")))
# export(str(reports.decide(2009, "/home/gergo/Desktop/5 th week/game_stat.txt")))
# export(str(reports.get_latest("/home/gergo/Desktop/5 th week/game_stat.txt")))
# export(str(reports.count_by_genre("/home/gergo/Desktop/5 th week/game_stat.txt", "First-person shooter")))
# export(str(reports.get_line_number_by_title("/home/gergo/Desktop/5 th week/game_stat.txt", "Diablo III")))


def menu():
    switch_on = 1
    while switch_on == 1:

        mode = input("Please give me a number of the function:")

        if mode in "1234567":
            if mode == "1":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    export(str(reports.count_games(information1)))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "2":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    export(str(reports.get_latest(information1)))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "3":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    information2 = input("Please give me the genre:")
                    export(str(reports.count_by_genre(information1, information2)))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "4":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    information2 = input("Please give me the title:")
                    export(str(reports.get_line_number_by_title(information1, information2)))
                except FileNotFoundError:
                    print ("Invalid input, please try again")
                    continue
            if mode == "5":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    export(str(reports.sort_abc(information1)))
                except:
                    print ("Invalid number, please try again")
                    continue

            if mode == "6":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    export(str(reports.get_genres(information1)))
                except:
                    print ("Invalid number, please try again")
                    continue
            
            if mode == "7":
                try:
                    information1 = input("Please give me the name of the txt file:")
                    export(str(reports.when_was_top_sold_fps(information1)))
                except:
                    print ("Invalid number, please try again")
                    continue
            
            
            exitQuestion = input("If would you like to ask another question please press 1 button and for exit push any other button: ")
            if exitQuestion != "1":
                switch_on += 1


menu()
