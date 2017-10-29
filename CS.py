'''
Goal: Display 2 graphs, 1 showing total winning team dmg dealt to champs across times, other showing total losing team dmg dealt to champs across times
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return list 3 nums [game length, avg CS of winning team at diff game durations, avg CS of losing team at diff durations]
'''
#0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
def CS(matchData):
    gameDuration = round(matchData["gameDuration"]/60)
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
        gameLength = ceil((gameDuration-20)/5)
    return [gameLength, winningTeamCS/numPlayersPerTeam, losingTeamCS/numPlayersPerTeam]
