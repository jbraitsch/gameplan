import requests

def get_teams_list():
    url = "https://records.nhl.com/site/api/franchise"
    r = requests.get(url)
    teams = r.json()["data"]
    teamNames = [x["fullName"] for x in teams if x["lastSeasonId"] == None]
    return teamNames

def get_team_abbrev(name):
    url = "https://records.nhl.com/site/api/franchise"
    r = requests.get(url)
    teams = r.json()["data"]
    teamAbbrev = ''
    for x in teams:
      if x["fullName"] == name:
        teamAbbrev = x["teamAbbrev"]
        return teamAbbrev
    return False

def get_team_schedule(abbrev):
  url = "https://api-web.nhle.com/v1/club-schedule/"+ abbrev +"/week/now"
  r = requests.get(url)
  schedule = r.json()["games"]
  games = []
  count = 0
  for x in schedule:
    year = ''
    month = ''
    day = ''
    hour = ''
    minute = ''
    date = x["gameDate"]
    for y in range(0,4):
      year = year + date[y]
    for m in range(5,7):
      month = month + date[m]
    for d in range(8,10):
      day = day + date[d]

    time = x["startTimeUTC"]
    for h in range(11,13):
      hour = hour + time[h]
    for m in range(14,16):
      minute = minute + time[m]
    
    if hour == "00":
      hour = "17"
    else:
        t = int(hour) -7
        hour = str(t)
    away = x["awayTeam"]["abbrev"]
    home = x["homeTeam"]["abbrev"]
    game = {"away":away, "home":home, "year":year, "month":month, "day":day, "hour":hour, "minute":minute}
    games.append(game)
    count = count+1
  return games