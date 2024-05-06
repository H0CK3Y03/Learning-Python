import random


number_of_teams = int(input("The number of player teams: "))
players = []
number = 0
teams = ()
number_of_players = int(input('The number of players participating: '))

for i in range(number_of_teams):
    team = (input(f"The {i+1}. team: "))
    team = ' '.join(team.split())
    teams += tuple(team)

while len(players) < number_of_players:
    number = random.randint(1, number_of_players)
    if number in players:
        continue
    else:
        players.append(number)

random.shuffle(players)
x = 1
y = 0

for team in teams:
    the_players = players[(len(players) // number_of_teams * y):(len(players) // number_of_teams) * x]
    x += 1
    y += 1
    print(f'The players on {team} team: {the_players}.')
    print(f'The number of players on {team} team: {len(the_players)}')

players.sort()
print(players)
print(len(players))
print(teams)


