import reports

filename = input("What is the name of the file? (example:game_stat.txt)\n")
try:
    test = open(filename)
    test.close()
except:
    print ("There is no such file!")
    exit()
while True:
    print ("1: Count of games in the file")
    print ("2: Is there a game from a given year")
    print ("3: Latest Game")
    print ("4: Count of games by the given genre")
    print ("5: Number of the given name")
    menu = input("Type in the number of the desired option from above, or anything else to quit:\n")
    try:
        menu = int(menu)
    except:
        print ("Quit!")
        break
    if menu > 5 or menu < 1:
        print ("Quit!")
        break
    if menu == 1:
        print (reports.count_games(filename))
    elif menu == 2:
        year = input("Which year?: ")
        try:
            year = int(year)
        except:
            print ("Invalid argument given!")
            break
        print (reports.decide(filename, year))
    elif menu == 3:
        print (reports.get_latest(filename))
    elif menu == 4:
        genre = input("Which genre?: ")
        print (reports.count_by_genre(filename, genre))
    elif menu == 5:
        title = input("Which game?: ")
        print (reports.get_line_number_by_title(filename, title))
    print ()
