import itertools

def calculate_possibilities(deck_size, max_connections):
    # Generate all possible combinations of connections for a card
    connections = list(range(1, max_connections + 1))
    all_card_combinations = list(itertools.product(connections, repeat=deck_size))
    
    # Calculate the number of possibilities for one player
    possibilities_one_player = len(all_card_combinations)
    
    # Calculate the number of possibilities for all four players
    possibilities_all_players = possibilities_one_player ** 4
    
    return possibilities_one_player, possibilities_all_players

def main():
    deck_size = 70
    max_connections = 4
    
    possibilities_one_player, possibilities_all_players = calculate_possibilities(deck_size, max_connections)
    
    print("Number of possibilities for one player:", possibilities_one_player)
    print("Number of possibilities for all four players:", possibilities_all_players)

if __name__ == "__main__":
    main()
