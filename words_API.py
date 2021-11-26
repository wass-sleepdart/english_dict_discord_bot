import requests
from pprint import pprint
import json
def get_definition(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "c28d3912b5msh098dac9629c9e1bp10f86bjsnf509f72d9bb1"
        }
    response = requests.request("GET", url, headers=headers,)
    json_to_dict=json.loads(response.text)
    definition=json_to_dict['definitions']
    return definition


