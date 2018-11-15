from operator import itemgetter
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

def decide(filename,year):
    open_file(filename)
    for i in range(len(open_file(filename))):
        if open_file(filename)[i][2] == (str(year)):
            return True
            break
    else:
        return False
        

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
        if open_file(filename)[i][0] == title:
            return (i+1)
            break

def sort_abc(filename): # buble sorttal lehet rendessen megcsinálni!!!!!!!!!!!
    open_file(filename)
    title = []
    for i in range(len(open_file(filename))):
        title.append(open_file(filename)[i][0])
    return (sorted(title))

def get_genres(filename):
    open_file(filename)
    genre = []
    for i in range(len(open_file(filename))):
        genre.append(open_file(filename)[i][3])
    genreSet = (set(genre))
    genreList = (list(genreSet))
    return (sorted(genreList))

def when_was_top_sold_fps(filename):
    fps = {}
    open_file(filename)
    for i in range(len(open_file(filename))):
        if open_file(filename)[i][3] == "First-person shooter":
            fps[open_file(filename)[i][1]] = open_file(filename)[i][2]
    sorterlist = []
    for element in range(len(fps)):
        sorterlist.append(float(list(fps.keys())[element]))
    result = (max(sorterlist))
    return (int(fps[str(result)]))
            




#get_genres("/home/gergo/Desktop/5 th week/game_stat.txt")

#when_was_top_sold_fps("/home/gergo/Desktop/5 th week/game_stat.txt")
# count_games("/home/gergo/Desktop/5 th week/game_stat.txt")
# decide(2009,"/home/gergo/Desktop/5 th week/game_stat.txt")
# get_latest("/home/gergo/Desktop/5 th week/game_stat.txt")
# count_by_genre("/home/gergo/Desktop/5 th week/game_stat.txt","First-person shooter")
# get_line_number_by_title("/home/gergo/Desktop/5 th week/game_stat.txt","Diablo III")
#sort_abc("/home/gergo/Desktop/5 th week/game_stat.txt")