import requests
from pprint import pprint
import json
def get_definition(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': ""#get you own api key
        }
    response = requests.request("GET", url, headers=headers,)
    json_to_dict=json.loads(response.text)
    definition=json_to_dict['definitions']
    return definition


