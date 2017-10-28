'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return a dictionary {winningTeamWardsPerMin, losingTeamWardsPerMin}
'''
def wardsPerMin(matchData)
  winLoseWards = {}
  matchID = matchData[matches][0]["gameID"]
  gameDuration = round(matchData["gameDuration"]/60)
  losingTeamNumWards = 0
  winningTeamNumWards = 0
  for i in range(len(participants))
    if (matchData[participants][i][stats]["win"])
      winningTeamWardsPerMin += (matchData[participants][i][stats]["wardsPlaced"]/gameDuration)
    else
      losingTeamWardsPerMin += (matchData[participants][i][stats]["wardsPlaced"]/gameDuration)
  winLoseWards["winningTeamWardsPerMin": winningTeamWardsPerMin]
  winLoseWards["losingTeamWardsPerMin": losingTeamWardsPerMin]
  return winLoseWards
