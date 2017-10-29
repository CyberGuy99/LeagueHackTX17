'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return a dictionary {winningTeamWardsPerMin, losingTeamWardsPerMin}
'''
import API

def wardsPerMin(gameId):
    '''
    input: gameId
    returns: list, [winningWPM,losingWPM,minutes] each is an int,
    last in game length in minutes
    '''
    match = API.getMatchData(gameId)
    matchTime = round(match["gameDuration"]/60)
    winningTeamWards = 0
    losingTeamWards = 0
    for participant in match["participants"]:
        if participant["stats"]["win"]:
            winningTeamWards += participant["stats"]["wardsPlaced"]
        else:
            losingTeamWards += participant["stats"]["wardsPlaced"]

    winningWPM = winningTeamWards/matchTime
    losingWPM = losingTeamWards/matchTime
    return [winningWPM,losingWPM,matchTime]

def main(): #Testing w/ Clayuh
    Clayuh = API.getSummonerDTO("Clayuh")
    gameList = API.makeGameList(Clayuh["accountId"])
    print(wardsPerMin(gameList[0]))

if __name__ == "__main__":
    main()
