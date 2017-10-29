import math
'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return a number indicating when game was won (0-8; -1 for loss)
'''
#0: <=20, 1: 20-25, 2: 25-30, 3: 30-35, 4:35-40, 5: 40-45, 6: 45-50, 7: 50-55, 8: 55<
def gameDuration(matchData,accountID):

  participantID = ""

  for participantIdentity in matchData["participantIdentities"]: #converts accountID to participantID
    if (participantIdentity["player"]["accountId"]==accountID):
      participantIdentity = participant["participantId"]
      break

  for participant in matchData["participants"]: #determines if game is win or loss
    if (participant["stats"][participantId] == participantID):
      win = participant["stats"]["win"]
      break

  gameDuration = math.round(matchData["gameDuration"]/60)

  if gameDuration<=20: #all times less than or equal to 20 are mapped to 0
    gameDuration = 0
  elif gameDuration> 55:
    gameDuration = 8
  else:
    gameDuration -= 20
    gameDuration = math.ceil(gameDuration/5) #5 min buckets

  if win:
    return gameDuration
  return -1

'''
Gets match info for all matches and gets win time in 0-8/-1 form
Then adds those times and averages into one list
Input: list of game ID numbers for a certain player, and account ID number for that player
Output: list of winrate for each game type (0-8)
'''
def winRates(gameIDs,accountID):
  matches = [getMatchData(gameID) for gameID in gameIDs]
  winTimes = [gameDuration(match,accountID) for match in matches]
  totalWinTime = [0]*9
  for winTime in winTimes:
    if(winTime!=-1)
      totalWinTime[winTime] += 1
  avgWinRate = [numGames/len(winTimes) for numGames in totalWinTime]
  return avgWinRate
