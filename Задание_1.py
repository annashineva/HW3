import requests


def most_intel_superhero(superheros_name):
    url = 'https://akabab.github.io/superhero-api/api/all.json' #задаем переменную для url
    response = requests.get(url=url) #получаем данные со страницы
    superheros_list = superheros_name.split(', ') #создаем переменную для списка с именами, которые задаем при перечислении супергероев
    superheros_intelligence = {} #создаем словарь, куда поместим имя и интеллект супергероя
    intelligence = [] #создаем список для значений интеллекта
    for i in response.json():
        if i.get('name') in superheros_list: #получаем имя супергероя и проверяем, есть ли оно в списке супергероев, который мы задали
            superheros_intelligence[i['name']] = i['powerstats']['intelligence'] #заполняем словарь именем и интеллектом супергероя
    for number in superheros_intelligence.values():
        intelligence.append(int(number)) #пополняем список со значениями интеллекта
    for key, value in superheros_intelligence.items(): #создаем цикл для сравнения максимального значения интеллека по списку со значениями словаря и выводим имя
        if value == max(intelligence):
            res = f'Самый умный супергерой - {key}'
    return print(res)


if __name__ == '__main__':
    most_intel_superhero('Captain America, Thanos, Hulk')