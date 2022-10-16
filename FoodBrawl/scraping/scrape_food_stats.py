from bs4 import BeautifulSoup
import requests

class get_food_stats:
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url

    def get_stat(self,  food_id, stat):
        url = self.url + food_id
        match stat:
            case "energy":
                stat_to_fetch = '"energy":'
            case "carbs":
                stat_to_fetch = '"carbohydrate":'
            case "protein":
                stat_to_fetch = '"protein":'
            case "fat":
                stat_to_fetch = '"fat":'

        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        parse_start = (str(soup).partition(stat_to_fetch)[2])
        result = int(float(parse_start.partition(",")[0]))
        print(result)
        return result