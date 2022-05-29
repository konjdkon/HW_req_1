import requests
import pandas as pd

class SuperHero:
    global url
    url = 'https://superheroapi.com/api/2619421814940190/'
    def __init__(self, name):
        self.name = name
        self.id = self.getid(name)
        self.intelligence = int(self.get_intelligence(self.id))
    def getid(self, name):
        method = 'search/'
        finalurl = url + method + name
        response = requests.get(finalurl)
        df = pd.read_json(response.text, orient='result')
        return df['results'][0]['id']
    def get_intelligence(self, id):
        method = '/powerstats'
        finalurl = url + str(id) + method
        response = requests.get(finalurl)
        df = pd.read_json(response.text, orient='index')
        return df[0]['intelligence']

def start():
    name = ['Hulk', 'Captain America', 'Thanos']
    intelligence_table = {}
    for i in range(len(name)):
        x = name[i]
        x = SuperHero(name[i])
        intelligence_table[name[i]] = x.intelligence
    print(max(intelligence_table, key=intelligence_table.get), intelligence_table[max(intelligence_table, key=intelligence_table.get)])

start()