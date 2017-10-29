'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return an array indicating when game is won {i.e. [1,0,0,0,0,0,0,0,0] means early game <=20 min with every bucket lasting 5 min}
'''
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

  gameDuration = round(matchData["gameDuration"]/60)
 
  if gameDuration<=20: #all times less than or equal to 20 are mapped to 0
    gameDuration = 0
  elif gameDuration>= 55:  
    gameDuration = 8
  else:
    gameDuration -= 20
    gameDuration = ceil(gameDuration/5) #5 min buckets

  if win:
    return gameDuration
  return -1

def winRates(matches,accountID):
  winTimes = [gameDuration(match,accountID) for match in matches]
  totalWinTime = [0]*9
  for winTime in winTimes:
    if(winTime!=-1)
      totalWinTime[winTime] += 1
  avgWinRate = [time/len(winTimes) for time in totalWinTime]
  return avgWinRate