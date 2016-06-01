import reports

file = open("exports.txt", 'w')
filename = input("What is the name of the file you want to export the reports from? (example:game_stat.txt)\n")
try:
    test = open(filename)
    test.close()
except:
    print ("There is no such file!")
    exit()
while True:
    print ("Exporting reports in the exports.txt file")
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
        file.write("Number of games: " + str(reports.count_games(filename)) + "\n")
    elif menu == 2:
        year = input("Which year?: ")
        try:
            year = int(year)
        except:
            print ("Invalid argument given!")
            break
        file.write("Is there a game from " + str(year) + ": " + str(reports.decide(filename, year)) + "\n")
    elif menu == 3:
        file.write("Latest game: " + reports.get_latest(filename) + "\n")
    elif menu == 4:
        genre = input("Which genre?: ")
        file.write("Number of " + genre + " games: " + str(reports.count_by_genre(filename, genre)) + "\n")
    elif menu == 5:
        title = input("Which game?: ")
        file.write("Number of " + title + ": " + str(reports.get_line_number_by_title(filename, title)) + "\n")
    print ("Exported!\n")
file.close()
