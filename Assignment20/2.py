class Chessplayer():
    def __init__(self, name="", year=0, rating=0):
        self.name = name
        self.year = year
        self.rating = rating

    def __str__(self):
        return "Name: {}\nYear: {}\nRating: {}".format(self.name, self.year, self.rating)


def get_highest_rated_player(players):
    highest_rated_player = Chessplayer()
    for player in players:
        if player.rating > highest_rated_player.rating:
            highest_rated_player = player
    return highest_rated_player

def get_average_rating(players):
    sum_of_ratings = 0
    for player in players:
        sum_of_ratings += player.rating
    return format(sum_of_ratings / len(players), '.2f')


def main():
    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here....
    while len(players) != number_of_players:
        name = input("Enter Name: ")
        year = int(input("Enter Year: "))
        rating = int(input("Enter Rating: "))
        player = Chessplayer(name, year, rating)
        players.append(player)
    
    print("--- Displaying players ---")
    for player in players:
        print(player)

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)

main()