
# Report functions


def count_games(filename):
    with open(filename) as f:
        content = f.readlines()
    return len(content)


def decide(filename, year):
    bool = False
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if int(game.split('\t')[2]) == year:
            bool = True
            break
    return bool


def get_latest(filename):
    latestyear = 0
    latestgame = ""
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if int(game.split('\t')[2]) > latestyear:
            latestyear = int(game.split('\t')[2])
            latestgame = game.split('\t')[0]
    return latestgame


def count_by_genre(filename, genre):
    count = 0
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if game.split('\t')[3] == genre:
            count += 1
    return count


def get_line_number_by_title(filename, title):
    with open(filename) as f:
        content = f.readlines()
    for i in range(0, len(content)):
        if content[i].split('\t')[0] == title:
            return i+1
    raise ValueError("There is no such game!")
