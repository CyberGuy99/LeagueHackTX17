'''
Loop through all the matches that Clayuh has played
Input: matchData is the dictionary you are taking in to analyze from the API
Output: Should return a dictionary {winTime: winTime}
'''
def gameDuration(matchData)
  winEarlyLate = {}
  gameDuration = round(matchData["gameDuration"]/60)
  winBefore20 = 0
  win20to25 = 0
  win25to30 = 0
  win30to35 = 0
  win35to40 = 0
  win40to45 = 0
  win45to50 = 0
  win50to55 = 0
  winAfter55 = 0
  for (i in range(len(matchData[participants])))
        if (gameDuration <= 20)
            winBefore20+=1
        else if (gameDuration <= 25)
            win20to25+=1
        else if (gameDuration <= 30)
            win25to30+=1
        else if (gameDuration <= 35)
            win30to35+=1
        else if (gameDuration <= 40)
            win35to40+=1
        else if (gameDuration <= 45)
            win40to45+=1
        else if (gameDuration <= 50)
            win45to50+=1
        else if (gameDuration <= 55)
            win50to55+=1
        else
            winAfter55+=1
  winEarlyLate["winBefore20": winBefore20]
  winEarlyLate["win20to25": win20to25]
  winEarlyLate["win25to30": win25to30]
  winEarlyLate["win30to35": win30to35]
  winEarlyLate["win35to40": win35to40]
  winEarlyLate["win40to45": win40to45]
  winEarlyLate["win45to50": win45to50]
  winEarlyLate["win50to55": win50to55]
  winEarlyLate["winAfter55": winAfter55]
  return winEarlyLate
