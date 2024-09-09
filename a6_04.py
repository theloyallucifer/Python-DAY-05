n = int(input("Enter the number of players: "))
cricket = {}
for _ in range(n):
    player_name = input("Enter the player's name: ")
    runs_scored = int(input(f"Enter the runs scored by {player_name}: "))
    cricket[player_name] = runs_scored

query_name = input("Enter the name of the player to query: ")
if query_name in cricket:
    print(cricket[query_name])
else:
    print("Not found!..")
