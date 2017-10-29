import API
import math

def main(): #Testing w/ Clayuh
    Clayuh = API.getSummonerDTO("Clayuh")
    gameList = API.makeGameList(Clayuh["accountId"])
    print("For gameId:", gameList[0],"\n wpmWin,wpmLose, and matchTime(min):",wardsPerMin(gameList[0]))

if __name__ == "__main__":
    main()

#-----------------------------Consolidation Functions Below---------------------------------------------------------------------------------------------#

def infoFromMatches(matchIDs, function):
'''
Allowed Functions: winType, wardsPerMin, dmgDealtToChamps, CS
Takes list of game/match id numbers and desired JSON block (function) and outputs block as list
'''
  matches = [API.getMatchData(gameID) for gameID in gameIDs]
  allInfo = [function(match) for match in matches]
  return allInfo


def totalDoubleBuckets(matchIDs,function):
'''
Allowed Functions: winType, wardsPerMin, dmgDealtToChamps, CS
Input: Multiple gameIDs which is converted to list of match informations
Goal: Display 2 graphs, 1 showing avg WPM per team categorized by game length
Output: Should return list 9 lists of 2 nums [[avg property of winning team at game duration 1, avg property of losing team at game duration 1], duration 2, ..., duration 9]
'''
  allInfo = infoFromMatches(matchIDs,function)
  buckets = [[0,0]]*9
    for info in allInfo:
        buckets[info[0]][0] += info[1]
        buckets[info[0]][1] += info[2]
    avg = [[singleVal/len(allInfo) for singleVal in bucket] for bucket in buckets]
    return avg

def winRates(gameIDs,accountID):
'''
Gets match info for all matches and gets win time in 0-8/-1 form
Then adds those times and averages into one list
Input: list of game ID numbers for a certain player, and account ID number for that player
Output: list of winrate for each game type (0-8)
'''
  winTimes = infoFromMatches(matchIDs,winType)
  totalWinTime = [0]*9
  for winTime in winTimes:
    if(winTime!=-1)
      totalWinTime[winTime] += 1
  avgWinRate = [numGames/len(winTimes) for numGames in totalWinTime]
  return avgWinRate

#----------------------FUNCTIONS BELOW------------------------------------------------------------------#

def winType(matchData,accountID):
'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return a number indicating when game was won (0-8; -1 for loss)
0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
'''
  participantID = ""
  gameLength = categorizeTime(minFromData(matchData))


  for participantIdentity in matchData["participantIdentities"]: #converts accountID to participantID
    if (participantIdentity["player"]["accountId"]==accountID):
      participantIdentity = participant["participantId"]
      break

  for participant in matchData["participants"]: #determines if game is win or loss
    if (participant["stats"][participantId] == participantID):
      win = participant["stats"]["win"]
      break

  gameDuration = math.round(matchData["gameDuration"]/60)

  if win:
    return gameLength
  return -1

def wardsPerMin(matchData):
    '''
    input: gameId
    returns: list, [minutes,winningWPM,losingWPM] each is an int,
    last in game length in minutes
    '''
    gameLength = categorizeTime(minFromData(matchData))

    winningTeamWards = 0
    losingTeamWards = 0
    for participant in matchData["participants"]:
        if participant["stats"]["win"]:
            winningTeamWards += participant["stats"]["wardsPlaced"]
        else:
            losingTeamWards += participant["stats"]["wardsPlaced"]

    return [matchTime,winningWPM/gameLength,losingWPM/gameLength]

def dmgDealtToChamps(matchData):
'''
Goal: Display 2 graphs, 1 showing total winning team dmg dealt to champs across times, other showing total losing team dmg dealt to champs across times
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return list 3 nums [game length, [dmg dealt in winning games at diff game durations],[dmg dealt in losing games in diff durations]]
More detailed output: [2,466,333]
0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
'''
    gameLength = categorizeTime(minFromData(matchData))
    
    winningTeamDmg = 0
    losingTeamDmg = 0
    
    for participant in matchData["participants"]:
        if (participant["stats"]["win"]):
            winningTeamDmg += participant["stats"]["totalDamageDealtToChampions"]
        else:
            losingTeamDmg += participant["stats"]["totalDamageDealtToChampions"]
    
    return [gameLength, winningTeamDmg, losingTeamDmg]

def CS(matchData):
'''
Input: single match information
Output: Should return list 3 nums [game length, avg CS of winning team at diff game durations, avg CS of losing team at diff durations]
0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
'''
    gameLength = categorizeTime(minFromData(matchData))

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
        
    return [gameLength, winningTeamCS/numPlayersPerTeam, losingTeamCS/numPlayersPerTeam]

#-----------------------Minor Helper Methods----------------------------------------------------------------

def minFromData(matchData):
  return math.round(matchData["gameDuration"]/60)

def categorizeTime(min):
  if (min <= 20): #all times less than or equal to 20 are mapped to 0
    return 0
  elif (min > 55): #all greater than 55 are mapped to 8
    return 8
  else:
    return math.ceil((gameDuration-20)/5) #5 min buckets