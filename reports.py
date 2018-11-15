
def open_file(filename):
    lines = []
    with open (str(filename)) as game_text:
        for line in game_text:
            lines.append(line.split('\t'))
        return (lines)
            

def count_games(filename):
    open_file (filename)
    #return (len(lines))
    return (len(open_file(filename)))

def decide(year,filename):
    open_file(filename)
    for i in range(len(open_file(filename))):
        if open_file(filename) [i][2] == (str(year)):
            return True
            break
        else:
            return False
            break

def get_latest(filename):
    open_file(filename)
    for i in range(len(open_file(filename))):
        all_year = []
        for i in range (len(open_file(filename))):
            all_year.append(open_file(filename)[i][2])
    last_year = (max(all_year)) 
    for i in range (len(open_file(filename))):
        if open_file(filename) [i][2] == (str(last_year)):
            return (open_file(filename) [i][0]) 
            break


def count_by_genre(filename,genre):
    open_file(filename)
    numberOfGenre = 0
    for i in range(len(open_file(filename))):
        if open_file(filename)[i][3] == genre:
            numberOfGenre += 1
    return (numberOfGenre)



def get_line_number_by_title(filename,title):
    for i in range(len(open_file(filename))):
        if open_file(filename) [i][0] == title:
            return (i+1)
            break


# count_games("/home/gergo/Desktop/5 th week/game_stat.txt")
# decide(2009,"/home/gergo/Desktop/5 th week/game_stat.txt")
# get_latest("/home/gergo/Desktop/5 th week/game_stat.txt")
# count_by_genre("/home/gergo/Desktop/5 th week/game_stat.txt","First-person shooter")
# get_line_number_by_title("/home/gergo/Desktop/5 th week/game_stat.txt","Diablo III")

