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

export(str(reports.count_games("/home/gergo/Desktop/5 th week/game_stat.txt")))
export(str(reports.decide(2009, "/home/gergo/Desktop/5 th week/game_stat.txt")))
export(str(reports.get_latest("/home/gergo/Desktop/5 th week/game_stat.txt")))
export(str(reports.count_by_genre("/home/gergo/Desktop/5 th week/game_stat.txt", "First-person shooter")))
export(str(reports.get_line_number_by_title("/home/gergo/Desktop/5 th week/game_stat.txt", "Diablo III")))
