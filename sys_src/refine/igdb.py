import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

class TwitchAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        # create authorization object
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

        # build login dictonary
        login = {'grant_type': 'client_credentials',
                "client_id": client_id,
                "client_secret": client_secret}
        
        headers = {"Client-ID": client_id}
        # send request for authorization token
        res = requests.post('https://id.twitch.tv/oauth2/token', auth=auth, data=login,)
        # get token and check if it is valid
        if res.status_code == 200:
            token = res.json()['access_token']
            print('Token acquired')
        else:
            print(res.status_code)
            print(res.json())
            raise Exception('Token not acquired')
        
        headers['Authorization'] = f'Bearer {token}'

        self.headers = headers
        self.api = 'https://api.igdb.com/v4'


    def get_games(self):
        # get all games
        query = 'fields name, id, first_release_date, cover.url, genres.name, platforms.name, summary, total_rating, involved_companies.company.name, involved_companies.developer, involved_companies.publisher, involved_companies.company.country; limit 500; where total_rating > 85; sort rating desc;'
        res = requests.post(self.api + '/games', headers=self.headers, data=query)
        if res.status_code == 200:
            print('Games acquired')
            with open('game_data.json', 'w') as f:
                json.dump(res.json(), f)
        else:
            print(res.status_code)
            print(res.json())
            raise Exception('Games not acquired')
        return res.json()


if __name__ == "__main__":
    api = TwitchAPI(CLIENT_ID, CLIENT_SECRET)
    api.get_games()
