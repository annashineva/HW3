import requests

with open('superhero_list', 'rb') as f:
    response = requests.put(url='https://akabab.github.io/superhero-api/api', f)
    response.raise_for_status()


def most_intel_superhero(superheros_name):
    superheros_intelligence = {}
    intelligence = []
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    superheros_list = superheros_name.split(', ')
    for superheros_name in response:
        intelligence = max(intelligence)
    print (f'Самый сильный супергерой - {superheros_name}')


if __name__ == '__main__':
    most_intel_superhero('Hulk', 'Captain America', 'Thanos')