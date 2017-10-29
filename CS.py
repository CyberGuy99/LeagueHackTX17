import math
from __future__ import division
'''
Input: single match information
Output: Should return list 3 nums [game length, avg CS of winning team at diff game durations, avg CS of losing team at diff durations]
'''
#0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
def CS(matchData):
    gameDuration = math.round(matchData["gameDuration"]/60)
    winningTeamCS = 0
    losingTeamCS = 0
    numPlayersPerTeam = len(matchData["participants"])/2
    for participant in matchData["participants"]:
        if (participant["stats"]["win"]):
            winningTeamCS += participant["stats"]["totalMinionsKilled"]
            winningTeamCS += participant["stats"]["neutralMinionsKilled"]
        else:
            losingTeamCS += participant["stats"]["totalMinionsKilled"]
            losingTeamCS += participant["stats"]["neutralMinionsKilled"]
    if (gameDuration < 20):
        gameLength = 0
    elif (gameDuration > 55):
        gameLength = 8
    else:
        gameLength = math.ceil((gameDuration-20)/5)
    return [gameLength, winningTeamCS/numPlayersPerTeam, losingTeamCS/numPlayersPerTeam]

'''
Input: Multiple gameIDs which is converted to list of match informations
Goal: Display 2 graphs, 1 showing avg cs per team categorized by game length
Output: Should return list 9 lists of 2 nums [[avg CS of winning team at game duration 1, avg CS of losing team at game duration 1], duration 2, ...]
'''
def totalCS(gameIDs):
    matches = [getMatchData(gameID) for gameID in gameIDs]
    allCS = [CS(match) for match in matches]
    CSBuckets = [[0,0]]*9
    for cs in allCS:
        CSBuckets[cs[0]][0] += cs[1]
        CSBuckets[cs[0]][1] += cs[2]
    avgCS = [sum(winLossCS)/len(winLossCS) for winLossCS in zip(*CSBuckets)]
    return avgCS