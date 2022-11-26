import requests
import json



url = 'https://api.igdb.com/v4/games'
data_field = "fields *; limit500;"
header = {
            'Client-Id': 'kjxgha9u54fhylp730q5t2p0yvn6jp', 
            'Authorization': 'Bearer hdejejche17vh16ttoy3i2v9da7bgw'
        }

r = requests.post(url, data=data_field, headers=header)

with open('sys_src/data_pipe/games.json', 'w') as f:
    json.dump(r.json(), f)

print(r.text)