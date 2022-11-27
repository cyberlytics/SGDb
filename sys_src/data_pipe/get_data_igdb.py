import requests
import json

client_id= "s0upfq8wje1y8i0rrzqn3rh2xxhilk"
client_secret= "dz8e2ku8clmcvuhaq7ld8r6shy1b6f"

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
        query = 'fields name, id, first_release_date, cover.url, genres.name, platforms.name, summary, involved_companies.company.name, involved_companies.developer, involved_companies.publisher, involved_companies.company.country; limit 500; sort first_release_date desc;'
        res = requests.post(self.api + '/games', headers=self.headers, data=query)
    def get_games(self):
        # get all games
        query = 'fields name, id, first_release_date, cover.url, genres.name, platforms.name, summary, involved_companies.company.name, involved_companies.developer, involved_companies.publisher, involved_companies.company.country; limit 500; sort first_release_date desc;'
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

twitch = TwitchAPI(client_id, client_secret)
games = twitch.get_games()
