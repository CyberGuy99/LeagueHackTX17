'''
Goal: Display 2 graphs, 1 showing total winning team dmg dealt to champs across times, other showing total losing team dmg dealt to champs across times
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return list 3 nums [game length, [dmg dealt in winning games at diff game durations],[dmg dealt in losing games in diff durations]]
More detailed output: [2,466,333]
'''
#0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
def dmgDealtToChamps(matchData):
    gameDuration = round(matchData["gameDuration"]/60)
    winningTeamDmg = 0
    losingTeamDmg = 0
    for participant in matchData["participants"]:
        if (participant["stats"]["win"]):
            winningTeamDmg += participant["stats"]["totalDamageDealtToChampions"]
        else:
            losingTeamDmg += participant["stats"]["totalDamageDealtToChampions"]
    if (gameDuration < 20):
        gameLength = 0
    elif (gameDuration > 55):
        gameLength = 8
    else:
        gameLength = ceil((gameDuration-20)/5)
    return [gameLength, winningTeamDmg, losingTeamDmg]
