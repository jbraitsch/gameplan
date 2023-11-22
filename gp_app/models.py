from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import AbstractBaseUser
import requests

CITIES = (
    ('Colorado Springs', 'Colorado Springs'),
    ('Denver', 'Denver'),
    ('Fort Collins', 'Fort Collins'))
'''
class City(models.Model):
    CITIES = (
    ('Colorado Springs', 'Colorado Springs'),
    ('Denver', 'Denver'),
    ('Fort Collins', 'Fort Collins'))
    name = models.CharField(choices=CITIES, max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("index-city", args=[str(self.__str__)])
    
'''


class Business(models.Model):
    ACTIVE = ((True,'True'), (False,'False'))
    name = models.CharField("Name", max_length=200)
    email = models.CharField("Email", max_length=200)
    #city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
    city = models.CharField("Location", choices=CITIES, max_length=200)
    address = models.CharField("Address", max_length=200)
    phone_number = models.CharField("Phone", max_length=10)
    is_open = models.BooleanField("Open", default=True, blank=True)
    about = models.TextField(blank=True)
    #password = models.CharField("", max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business-detail', args=[str(self.id)])
    
    
class NHLTeam(models.Model):
    TEAMS = (('Montréal Canadiens', 'Montréal Canadiens'), ('Toronto Maple Leafs', 'Toronto Maple Leafs'), 
             ('Boston Bruins', 'Boston Bruins'), ('New York Rangers', 'New York Rangers'), ('Chicago Blackhawks', 'Chicago Blackhawks'), 
             ('Detroit Red Wings', 'Detroit Red Wings'), ('Los Angeles Kings', 'Los Angeles Kings'), ('Dallas Stars', 'Dallas Stars'), 
             ('Philadelphia Flyers', 'Philadelphia Flyers'), ('Pittsburgh Penguins', 'Pittsburgh Penguins'), 
             ('St. Louis Blues', 'St. Louis Blues'), ('Buffalo Sabres', 'Buffalo Sabres'), ('Vancouver Canucks', 'Vancouver Canucks'), 
             ('Calgary Flames', 'Calgary Flames'), ('New York Islanders', 'New York Islanders'), 
             ('New Jersey Devils', 'New Jersey Devils'), ('Washington Capitals', 'Washington Capitals'), ('Edmonton Oilers', 'Edmonton Oilers'), 
             ('Carolina Hurricanes', 'Carolina Hurricanes'), ('Colorado Avalanche', 'Colorado Avalanche'), ('Arizona Coyotes', 'Arizona Coyotes'), 
             ('San Jose Sharks', 'San Jose Sharks'), ('Ottawa Senators', 'Ottawa Senators'), ('Tampa Bay Lightning', 'Tampa Bay Lightning'), 
             ('Anaheim Ducks', 'Anaheim Ducks'), ('Florida Panthers', 'Florida Panthers'), ('Nashville Predators', 'Nashville Predators'), 
             ('Winnipeg Jets', 'Winnipeg Jets'), ('Columbus Blue Jackets', 'Columbus Blue Jackets'), ('Minnesota Wild', 'Minnesota Wild'), 
             ('Vegas Golden Knights', 'Vegas Golden Knights'), ('Seattle Kraken', 'Seattle Kraken'))
    name = models.CharField("Name", choices=TEAMS, max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('nhl_team_details', args=[str(self.id)])
    
    def get_team_abbrev(self):
        url = "https://records.nhl.com/site/api/franchise"
        r = requests.get(url)
        teams = r.json()["data"]
        teamAbbrev = ''
        for x in teams:
            if x["fullName"] == self.name:
                teamAbbrev = x["teamAbbrev"]
        return teamAbbrev
    
    def get_week_schedule(self, abbrev):
        url = "https://api-web.nhle.com/v1/club-schedule/"+ abbrev +"/week/now"
        r = requests.get(url)
        schedule = r.json()["games"]
        games = []
        count = 0
        for x in schedule:
            date = x["gameDate"]
            year = ''
            month = ''
            day = ''
            for y in range(0,4):
                year = year + date[y]
            for m in range(5,7):
                month = month + date[m]
            for d in range(8,10):
                day = day + date[d]

            time = x["startTimeUTC"]
            hour = ''
            minute = ''
            for h in range(11,13):
                hour = hour + time[h]
            for m in range(14,16):
                minute = minute + time[m]
    
            if int(hour) < 7:
                hour = str(24 + (int(hour) - 7))
            else:
                hour = str(int(hour) -7)

            time_of_day = 'am'
            if int(hour) > 12:
                hour = str(int(hour) - 12)
                time_of_day = 'pm'

            away = x["awayTeam"]["abbrev"]
            home = x["homeTeam"]["abbrev"]
            game = {"away":away, "home":home, "year":year, "month":month, "day":day, "hour":hour, "minute":minute, "time_of_day": time_of_day}
            games.append(game)
        return games
    

class User(AbstractBaseUser):
    username = models.CharField("Username", max_length=50)
    USERNAME_FIELD = "username"
    password = models.CharField("Password", max_length=200, default=None)
    email = models.CharField("Email", max_length=50)
    fav_team = models.ForeignKey(NHLTeam, on_delete=models.SET_DEFAULT, default = None, blank=True)
    fav_biz = models.ForeignKey(Business, on_delete=models.SET_DEFAULT, default = None, blank=True)
    

