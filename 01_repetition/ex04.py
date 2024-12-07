from file_with_this import teams, players
import json
from pprint import pprint

teams_dict = json.loads(teams)
players_dict = json.loads(players)


def find_comand(name: str) -> str:
    my_id = ''
    for person in players_dict:
        if person['name'] == name:
            my_id = person['team_id']
            break

    if my_id:
        for team in teams_dict:
            if team['id'] == my_id:
                return team['name']
    else:
        return 'Player was not found'


person_to_find = input()
print(find_comand(person_to_find))



'''
import json

name_player = input()
answer = 'Player was not found'

for player in json.loads(players):
    if name_player == player['name']:
        for team in json.loads(teams):
            if player['team_id'] == team['id']:
                answer = team['name']

print(answer)
'''