import requests


class SteamWebApi:
    api_key: str = '2OEIYCPSNRMH6CFG'
    base_url: str = 'https://www.steamwebapi.com/steam/api/'

    def __init__(self, api_key: str = None, debug: bool = False):
        """
        :param api_key: str
        :param debug: bool
        """
        if api_key is not None:
            self.api_key = api_key

        self.debug = debug

    def _get_inventory_request(self, steam_id: str, game: str = 'csgo', language: str = 'english', parse: bool = True):
        """
        :param steam_id: str
        :param game: str
        :param language: str
        :param parse: str
        :return: Response
        """
        if self.debug:
            print(
                f'GET {self.base_url}inventory?steam_id={steam_id}&game={game}&language={language}&parse={parse}'
                f'&key={self.api_key}')

        response = requests.get(f'{self.base_url}inventory', params={
            'steam_id': steam_id,
            'game': game,
            'language': language,
            'parse': parse,
            'key': self.api_key
        })

        if self.debug:
            print(f'Status Code: {response.status_code}')

        return response

    def get_inventory(self, steam_id: str, game: str = 'csgo', language: str = 'english', parse: bool = True):
        """
        :param steam_id: str
        :param game: str
        :param language: str
        :param parse: str
        :return: list
        """
        response = self._get_inventory_request(steam_id, game, language, parse)

        return response.json()

    def get_inventory_worth(self, steam_id: str, game: str = 'csgo', language: str = 'english', parse: bool = True):
        """
        :param steam_id: str
        :param game: str
        :param language: str
        :param parse: bool
        :return: dict
        """
        response = self._get_inventory_request(steam_id, game, language, parse)
        inventory = response.json()

        return {
            'worth': sum(float(item['priceAvg']) for item in inventory),
            'inventory': inventory
        }

    def get_steam_id(self, steam_id: str):
        """
        :param steam_id: str
        :return: dict
        """
        if self.debug:
            print(f'GET {self.base_url}steamid?steam_id={steam_id}&key={self.api_key}')

        response = requests.get(f'{self.base_url}steamid', params={
            'steam_id': steam_id,
            'key': self.api_key
        })

        if self.debug:
            print(f'Status Code: {response.status_code}')

        return response.json()

    def get_profile(self, steam_id: str, url_or_username: str = None):
        """
        :param steam_id: str
        :param url_or_username: str
        :return: dict
        """
        if self.debug:
            print(f'GET {self.base_url}profile?steam_id={steam_id}&url={url_or_username}&key={self.api_key}')

        response = requests.get(f'{self.base_url}profile', params={
            'steam_id': steam_id,
            'url': url_or_username,
            'key': self.api_key
        })

        if self.debug:
            print(f'Status Code: {response.status_code}')

        return response.json()
