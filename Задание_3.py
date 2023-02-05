from pprint import pprint

import requests


def get_all_queries():
    params = {
        'fromdate': '1675382400',
        'order': 'desc',
        'min': '1675555200',
        'sort': 'activity',
        'tagged': 'python',
        'site': 'stackoverflow'
    }
    req = requests.get('https://api.stackexchange.com/2.3/questions', params).json()
    req = req['items']['title']
    return pprint(req)


get_all_queries()
