#File containing methods to pull & manipulate JSON data from the Riot API

import requests

APIKey = "RGAPI-b4e2938b-12ff-4321-a0cc-b5d651c381c5"

def getSummonerDTO(summoner):
    '''
    summoner: int or string, can be either accountId, summonerName, or summonerId
    returns: summonerDTO(a JSON file representing a summoner as specified in summoner-v3)
    as a dictionary
    '''
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner
    r = requests.get(URL, params = {"api_key":APIKey})
    return r.json()

def getMatchlistDTO(accountId):
    '''
    accountId: int from summonerDTO
    returns: dict,matchDTO, as defined in API
    '''
    URL = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accountId)
    r = requests.get(URL, params = {"api_key":APIKey})
    return r.json()

def makeGameList(accountId):
    '''
    accountId: int, from summonerDTO
    returns: list of past 100 games represented as gameIds
    '''
    matchlistDTO = getMatchlistDTO(accountId)
    matches = matchlistDTO["matches"]
    games = []
    for match in matches:
        games.append(match["gameId"])
    return games

def getMatchData(gameId):
    '''
    gameId: int, object in gameList or matchDTO["matches"][x][gameId]
    returns: dict, matchDTO, as specified in the API (/lol/match/v3/matches/{matchId})
    '''
    URL = "https://na1.api.riotgames.com/lol/match/v3/matches/" + str(gameId)
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
