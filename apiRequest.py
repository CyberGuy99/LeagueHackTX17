#File containing methods to pull JSON data from the Riot API

import requests

APIKey = "RGAPI-b4e2938b-12ff-4321-a0cc-b5d651c381c5"

def getSummonerData(summoner):
    '''
    summoner: int or string, can be either accountId, summonerName, or summonerId

    returns: summonerDTO(a JSON file representing a summoner as specified in summoner-v3)
    as a dictionary
    '''
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner
    r = requests.get(URL, params = {"api_key":APIKey})
    return r.json()

'''
Example usage of getSummonerData shown below, other functions *should* work the
same way.

Clayuh = getSummonerData("Clayuh")

print("Summoner Name: ", Clayuh["name"])
print("Summoner Level: ", Clayuh["summonerLevel"])
print("Summoner ID: ", Clayuh["id"])

Console output:
Summoner Name:  Clayuh
Summoner Level:  30
Summoner ID:  37370842
'''
