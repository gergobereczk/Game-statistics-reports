import reports
import os

first_try = reports.count_games()

print (first_try)

# myfile = open("exportTXTversion.txt", "w")
# myfile.write(str(first_try))
# myfile.close()
# os.startfile("exportTXTversion.txt")

open ("/home/gergo/Desktop/5 th week/1.txt", "w")

if os.path.exists("/home/gergo/Desktop/5 th week/1.txt"):
    with open ("/home/gergo/Desktop/5 th week/1.txt", "a") as f:
        f.write(str(first_try))    

with open ("/home/gergo/Desktop/5 th week/1.txt", "w") as k:
    k.write (str(first_try))

#reports.count_games()
# Export functions
